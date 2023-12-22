/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState } = owl;

class Noticias extends Component {
    setup() {
        this.state = useState({value:1});
    }
}
    
Noticias.template = 'owl.Noticias';
registry.category('actions').add('owl.action_Noticias_js', Noticias);