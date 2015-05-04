/*
    Author  : Michael Janea (https://facebook.com/mbjanea)
    Version : 1.0
*/

CKEDITOR.plugins.add('fontawesome', {
    requires: 'widget',
    icons   : 'fontawesome',
    init    : function(editor){
        editor.widgets.add('FontAwesome', {
            button          : 'Insert Font Awesome',
            template        : '<span class="" style=""></span>',
            dialog          : 'fontawesomeDialog',
            allowedContent  : 'span(!fa){style}',
            upcast          : function(element){
                return element.name == 'span' && element.hasClass('fa');
            },
            init            : function(){
                this.setData('class', this.element.getAttribute('class'));
                this.setData('color', this.element.getStyle('color'));
                this.setData('size', this.element.getStyle('font-size'));
            },
            data            : function(){
                var istayl = '';
                this.element.setAttribute('class', this.data.class);
                istayl += this.data.color != '' ? 'color:' + this.data.color + ';' : '';
                istayl += this.data.size != '' ? 'font-size:' + parseInt(this.data.size) + 'px;' : '';
                istayl != '' ? this.element.setAttribute('style', istayl) : '';
                istayl == '' ? this.element.removeAttribute('style') : '';
            }
        });
        
        CKEDITOR.dialog.add('fontawesomeDialog', this.path + 'dialogs/fontawesome.js');
        CKEDITOR.document.appendStyleSheet('/static/css/font-awesome.min.css');
    }
});
