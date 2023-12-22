/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState } = owl;

class App extends Component {
    setup() {
        this.state = useState({value:1});
    }
}
    
App.template = 'owl.App';
registry.category('actions').add('owl.action_App_js', App);