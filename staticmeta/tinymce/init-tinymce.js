tinymce.init({
    /* replace textarea having class .tinymce with tinymce editor tinymce*/
    selector: "textarea.tinymce4-editor",

    /* theme of the editor */
    theme: "modern",
    skin: "lightgray",

    /* width and height of the editor */
    width: "50%",
    height: 300,


    /* display statusbar */
    statubar: true,

    /* plugin */
    plugins: [
        "advlist anchor autolink autoresize autosave bbcode charmap code codesample colorpicker ",
        "contextmenu directionality emoticons example example_dependency fullpage fullscreen hr ",
        "image imagetools importcss insertdatetime layer legacyoutput link lists media nonbreaking ",
        "noneditable pagebreak paste preview print save searchreplace spellchecker tabfocus table   ",
        "template textcolor textpattern visualblocks visualchars wordcount"
    ],
    toolbar: " forecolor backcolor removeformat | insertfile undo redo | styleselect | bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | pagebreak | fontselect fontsizeselect formatselect | charmap emoticons | fullscreen  preview save print | insertfile image media template link anchor codesample | ltr rtl",

    /* css Import-- */
    content_css: [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
        '//www.tiny.cloud/css/codepen.min.css',
        'https://www.w3schools.com/w3css/4/w3.css',
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'
    ],

    //content_css_cors: true,

    /* Image--------------------------------------------> */
    image_title: true,
    // enable automatic uploads of images represented by blob or data URIs
    automatic_uploads: true,
    // add custom filepicker only to Image dialog
    file_picker_types: 'image',
    file_picker_callback: function(cb, value, meta) {
        var input = document.createElement('input');
        input.setAttribute('type', 'file');
        input.setAttribute('accept', 'image/*');

        input.onchange = function() {
            var file = this.files[0];
            var reader = new FileReader();

            reader.onload = function() {
                var id = 'blobid' + (new Date()).getTime();
                var blobCache = tinymce.activeEditor.editorUpload.blobCache;
                var base64 = reader.result.split(',')[1];
                var blobInfo = blobCache.create(id, file, base64);
                blobCache.add(blobInfo);
                //console.log(base64);
                // call the callback and populate the Title field with the file name
                cb(blobInfo.blobUri(), { title: file.name });
            };
            reader.readAsDataURL(file);
        };

        input.click();
    },

    /* //Image Bootstrap Class Add set */
    image_class_list: [
        { title: 'None', value: '' },

        //Bootstrap Design
        { title: 'img-rounded', value: 'img-rounded' },
        { title: 'img-circle', value: 'img-circle' },
        { title: 'img-thumbnail', value: 'img-thumbnail' },
        { title: 'img-responsive', value: 'img-responsive' },

        //Design
        { title: 'w3-round', value: 'w3-round' },
        { title: 'w3-circle', value: 'w3-circle' },
        { title: 'w3-border w3-padding', value: 'w3-border w3-padding' },

        //Color
        { title: 'w3-sepia-min', value: 'w3-sepia-min' },
        { title: 'w3-sepia', value: 'w3-sepia' },
        { title: 'w3-sepia-max', value: 'w3-sepia-max' },

        //hover effect
        { title: 'w3-hover-opacity', value: 'w3-hover-opacity' },
        { title: 'w3-hover-grayscale', value: 'w3-hover-grayscale' },
        { title: 'w3-hover-sepia', value: 'w3-hover-sepia' },

        //Opacity
        { title: 'w3-opacity-min', value: 'w3-opacity-min' },
        { title: 'w3-opacity', value: 'w3-opacity' },
        { title: 'w3-hover-sepia', value: 'w3-opacity' }

    ],

    /*  Template Add--  */
    templates: [{
            title: 'Primary panel',
            description: 'panel',
            content: '<div class="panel panel-primary"><div class= "panel-heading"> <span class="fa fa-info">&nbsp;Details</span></div><div class="panel-body"></div></div></div>'
        },
        { title: 'Template I', description: 'Blog Template', url: '../media/tiny_template/Blog_Tempale_I.html' },
        { title: 'Template II', description: 'Catering Tempale', url: '../static/TinyTemplate/Catering_Tempale.html' },
        { title: 'Template III', description: 'Summer Holiday', url: 'static/tinymce/TinyTemplate/Summer_Holiday.html' },
        { title: 'Template II', description: 'Profile', url: 'tinymce/TinyTemplate/Profile_I.html' }

    ],


    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
    noneditable_noneditable_class: "mceNonEditable",
    toolbar_drawer: 'sliding',
    contextmenu: "link image imagetools table",



    image_caption: true,
    toolbar_sticky: true,
    image_advtab: true,
    importcss_append: true,

    /* bootstrap add ------------------->*/
    visual_table_class: 'table-responsive table table-bordered w3-table-all',
    valid_elements: ''
        //autosave_ask_before_unload: true,
        //autosave_interval: "30s",
        //autosave_prefix: "{path}{query}-{id}-",
        //autosave_restore_when_empty: false,
        //autosave_retention: "2m",
});