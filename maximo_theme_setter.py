import cssutils
import get_hue_shift

maximo_base_color = "#4177BD"
maximo_theme = {
    "primary": "#5c2d91",
        #"onPrimary": "",
    "secondary": "#92278f",
        #"onSecondary": "",
    "tertiary": "#962071",
        #"onTertiary": "",
        
    "hover": "#dbb3e4",
    "selected": "#e8d9eb"
}

# Dictionary of what attribute to change in which selector to what color
element_classification = {
    "primary": [
                ('.tc .label', 'color', ''),
                ('.bgnbp', 'background-color', ''),
                ('.umtable', 'border-color', ''),
                ('.pbspecial', 'background-image', '-moz-linear-gradient(var(--secondary) 1px, var(--primary) 100%)')
                ('.tabgroupback, .scTabGroup', 'background', 'url("../images/tabgroup/iot18_tabgroup_back.png") repeat-x scroll left bottom var(--primary)'),
                ('.subtabgroupback', 'background', 'url("../images/tabgroup/iot18_tabgroup_back.png") repeat-x scroll left bottom var(--primary)'),
                ('.tabgroup LI', 'background', ''),
                ('.tton', 'color', ''),
                ('.ttoff:hover', 'color', ''),
                ('.ttoffhover', 'color', ''),
                ('.helpgrid', 'color', ''),
                ('.help', 'color', ''),
                ('', 'background', '')
                ],
        #"onPrimary": [()],
    # "secondary": [('','')],
    #     #"onSecondary": [()],
    # "tertiary": [('','')],
    #     #"onTertiary": [()],
    # "hover": [('','')],
    # "selected": [('','')]
}

shift = get_hue_shift.main(maximo_base_color, maximo_theme['primary'])
image_elements = []

def main():
    cssfile = cssutils.parseFile("maximo_backup.css")
    
    insert_theme_variables(cssfile)
        
    refractor_element_colors(cssfile, extract_rule_indices(cssfile))
    
    shift_image_hues(cssfile, image_elements)
    
    with open('output.css', 'wb') as f:
        f.write(cssfile.cssText)
    
def extract_rule_indices(cssfile: cssutils.css.CSSStyleSheet):
    rule_indices = {}
    for i, rule in enumerate(cssfile.cssRules):
        if type(rule) is cssutils.css.CSSStyleRule:
            rule_indices[rule.selectorText] = i            
    return rule_indices

def insert_theme_variables(cssfile: cssutils.css.CSSStyleSheet):
    #Create the style declaration and populate it
    style = cssutils.css.CSSStyleDeclaration('')
    for key in maximo_theme:
        style[f'--{key}'] = f'{maximo_theme[key]}'
        
    #Create the rule with the ':root' selector and set the above style declaration
    rule = cssutils.css.CSSStyleRule(':root', style)
    cssfile.insertRule(rule, 3)
    
def refractor_element_colors(cssfile: cssutils.css.CSSStyleSheet, rule_indices):
    for elements_of_class in element_classification:
        for element, attribute, custom_value in element_classification[elements_of_class]:
            rule_index = rule_indices[element]
            rule = cssfile.cssRules[rule_index]
            
            # Set the value to the class of the element if it doesnt have a custom value, otherwise set the value to the custom value
            rule.style[attribute] = f'var(--{elements_of_class})' if custom_value == '' else custom_value
                

def shift_image_hues(cssfile: cssutils.css.CSSStyleSheet, rule_indices):
    return

if __name__ == "__main__":
    main()