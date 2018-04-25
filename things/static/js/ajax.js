$(document).ready(function(){
    $(function () {
    $.ajaxSetup({
        method: "post",
        error : function(res, err) {
            alert('Form submission failed please fill form corectly again.')
        },
        success: function(res) {
            console.log(res['error'])
            if (res['error'] == 'none') {
                $('#modal-success').modal();
                $('#modal-success').modal('open');
                $('input[name="title"]').val('')
                $('textarea[name="description"]').val('')
                $('input[name="author_email"]').val('')
                document.activeElement.blur();
            } else {
                $('#modal-error').modal();
                $('#modal-error').modal('open');
            }
        }
    });
});
});


function createThing(e) {
    e.preventDefault();
    var title=$('input[name="title"]'),
    description=$('textarea[name="description"]'),
    authorEmail=$('input[name="author_email"]');
    
        $.ajax({
        url : '/ajax/create_thing',
        data :{ 'title': title.val(),
        'description':description.val(),
        'author_email':authorEmail.val()
        }
        })  
    
}



function editThing(e) {
    e.preventDefault();
    var title=$('input[name="title"]'),
    description=$('textarea[name="description"]'),
    authorEmail=$('input[name="author_email"]'),
    slug = $('input[name="slug"]');
        $.ajax({
        url : '/ajax/edit_thing',
        data :{ 'title': title.val(),
        'description':description.val(),
        'author_email':authorEmail.val(),
        'slug':slug.val()
        }
        })
    
}

function sendEmail(e) {
     e.preventDefault();
     var title=$('input[name="title"]'),
    body=$('textarea[name="body"]'),
    from_=$('input[name="from_"]'),
    id = $('input[name="id"]');
        $.ajax({
        url : '/ajax/contact_author',
        data :{ 'title': title.val(),
        'body':body.val(),
        'from_':from_.val(),
        'id':id.val()
        }
        })
    
}


