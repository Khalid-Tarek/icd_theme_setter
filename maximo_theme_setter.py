import json
import cssutils
import get_hue_shift

def main():
    theme = extract_theme("theme_variables.json")
    
    main_file_path = f'{theme["file_paths"]["maximo"]}.css'
    #login_file_path = f'{theme["file_paths"]["login"]}.css' TODO: Login Theme Functionality
    
    #create_backup_files(theme, main_file_path, login_file_path) TODO: Login Theme Functionality
    
    apply_theme("Main", theme, main_file_path)
    
    #apply_theme("Login", theme, login_file_path) TODO: Login Theme Functionality

def create_backup_files(theme: dict, main_file_path: str, login_file_path:str):
    main_file_backup_path = f'{theme["file_paths"]["maximo"]}_backup.css'
    login_file_backup_path = f'{theme["file_paths"]["login"]}_backup.css'
    
    with open(main_file_backup_path, 'w') as backup:
        with open(main_file_path, 'r') as f:
            backup.write(f.read())
            
    with open(login_file_backup_path, 'w') as backup:
        with open(login_file_path, 'r') as f:
            backup.write(f.read())

def extract_theme(file_path:str):
    theme = json.load(open(file_path))
    
    #Change each color role's elements' representation from array to tuple
    for role_elements in theme["role_elements"]:
        for element in role_elements:
            element = tuple(element)
            
    return theme

def apply_theme(on: str, theme: dict, filepath: str):
    cssfile = cssutils.parseFile(filepath)
    insert_theme_variables(cssfile, theme)
    rule_indices = extract_rule_indices(cssfile)
    
    if on.lower() in ("main", "maximo"):
        refractor_elements(cssfile, theme, rule_indices)
        shift_image_hues(cssfile, theme, rule_indices)
    elif on.lower() in ("login"):
        # TODO: Login Theme Functionality 
        return    
    
    #TODO: Uncomment this line and remove the one after, when you're done testing
    #with open(filepath, 'wb') as f:
    with open('maximo.css', 'wb') as f:
        f.write(cssfile.cssText)

def insert_theme_variables(cssfile: cssutils.css.CSSStyleSheet, theme: dict):
    """
    Adds a root element to the document with the theme variables
    """
    #Create the style declaration and populate it
    style = cssutils.css.CSSStyleDeclaration('')
    for key in theme["maximo_theme"]:
        style[f'--{key}'] = f'{theme["maximo_theme"][key]}'
        
    #Create the rule with the ':root' selector and set the above style declaration
    rule = cssutils.css.CSSStyleRule(':root', style)
    cssfile.insertRule(rule, 3)
    
def extract_rule_indices(cssfile: cssutils.css.CSSStyleSheet):
    """
    Creates a dictionary that maps all element names to their indices in the rule list.
    
    Library Explanation
    ------------
    - CSSStyleSheet:              Representation of the entire CSS document in the form of a list of "CSSRule"s
    - CSSRule:                     A segment of the CSSStyleSheet. The following types of rules are what we could care about:
        - CSSStyleRule:             The standard type of CSSRule. It's seperated into "Selector Text" and "CSSStyleDeclaration".
            - Selector Text:        The part of the rule that identifies the element, class or id on which the following block will apply the style on
            - CSSStyleDeclaration:  The part of the rule where the actual style is specified. It's represented as a dictionary.
        - CSSCommentRule:           A segment that contains a comment. We don't make use of it in this script but perhaps it could be useful
        
    Function's Purpose
    ------------
    Since the cssRules list is a list, it doesn't make sense to keep searching for the specific rule by selector.
    Therefore, I pass by the cssRules list once, checking if the rule is a CSSStyleRule, and adding it's index to the dictionary like so:
    - {"selectorText":"index"}
    """
    
    rule_indices = {}
    for i, rule in enumerate(cssfile.cssRules):
        if type(rule) is cssutils.css.CSSStyleRule:
            rule_indices[rule.selectorText] = i            
    return rule_indices

def refractor_elements(cssfile: cssutils.css.CSSStyleSheet, theme: dict, rule_indices: dict[str, int]):
    """
    Iterates over all the roles and the elements specified to be sets their attribute to passed value.
    If the passed value is empty, simply sets the attribute's value to "var(--role)"
    """
    
    for role in theme["role_elements"]:
        for element, attribute, custom_value in theme["role_elements"][role]:
            
            if element == "": 
                continue
            
            rule_index = rule_indices[element]
            rule = cssfile.cssRules[rule_index]
            
            # Set the value to the role of the element if it doesnt have a custom value, otherwise set the value to the custom value
            rule.style[attribute] = f'var(--{role})' if custom_value == '' else custom_value
                
def shift_image_hues(cssfile: cssutils.css.CSSStyleSheet, theme: dict, rule_indices: dict[str, int]):
    """
    TODO: Simplies adds a filter over all the selected images:
    
    filter: hue-shift(<shift>)
    """
    
    shift = get_hue_shift.main(theme["maximo_base_color"], theme["maximo_theme"]["primary"])

if __name__ == "__main__":
    main()