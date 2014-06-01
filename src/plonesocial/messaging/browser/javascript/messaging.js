
var recipient = ''


function messaging_ajax_post (url, data) {
    // default ajax query
    $.ajax({
       type: "POST",
       url: url,
       data: data,
       success: function(data) {

       }
    });
}


function messaging_ajax (url, replaceid, datatype, contentid) {
    // default ajax query
    $.ajax({
       type: "GET",
       dataType: datatype,
       url: url,
       success: function(data) {
           if (datatype == 'html') {
               if (replaceid == '#personaltools-plone_social_menu') {
                   add_inbox_count(data);
               }
               else if (contentid) {
                   $(replaceid).replaceWith($(data).find('#content').html());
               }
               else {
                   $(replaceid).replaceWith(data);
               }
           }
           send_new_message();
           format_send_form()

       }
    });
}

function format_send_form() {
    // format send message form when reply button has been activated
    if (('#form-widgets-recipient').length > 0) {
        $('#conversation-content h1').remove();
        $('#form-widgets-recipient').val(recipient);
        $('#formfield-form-widgets-recipient label').hide();
        var recipient_input = $('#form-widgets-recipient').clone();
        $(recipient_input).attr('type','hidden');
        $('#form-widgets-recipient').remove();
        $('#formfield-form-widgets-recipient').append(recipient_input);
        $('#formfield-form-widgets-recipient').parent().submit(function(event){
            event.preventDefault();
            reload_messages();
        });
    }
}

function reload_messages() {
    // show full view of the inbox
    $('#content').empty();
    messaging_ajax('@@social-inbox?view=full', '#content', 'html', true);
    $('#your-messages').toggle();
}

function message_click() {
    // show mini view of the inbox
    $('#your-messages .messages').empty();
    messaging_ajax('@@social-inbox?view=small', '#your-messages .messages', 'html', true);
    $('#your-messages').toggle();
}


function add_inbox_count(data) {
    // simple inbox number look up
    var msg_count = data.trim();
    if (msg_count) {
        $('#personaltools-plone_social_menu a').append(" (" + msg_count + ")");
    }
}


function send_new_message(){
    // create overlay of send messages
    $('#inbox-new-message a').prepOverlay({
        subtype: 'ajax',
        filter: '#content > *',
    });
}


function send_message_full() {
    // apply send message screen to main content
    $('#conversation-content').empty();
    messaging_ajax('@@messaging-send', '#conversation-content', 'html', true);
    return false;
}


$(document).ready(function(){

    $('#inbox-new-message-full').live('click', send_message_full);

    if ($('#personaltools-plone_social_menu').length > 0) {
        // if there is a social menu link, then add number of unread messages
        messaging_ajax('@@your-messages?count=true', '#personaltools-plone_social_menu', 'html');

    }
    if ($('#show-your-messages').length > 0) {
        // if there is a inbox icon, then load the messages inbox details
        messaging_ajax('@@your-messages', '#show-your-messages', 'html');
        $('#your-messages-icon').live('click', message_click);
    }

    if ($('#inbox-reply-message-full').length > 0) {
        // if there is a reply button, replace it with the message form
        recipient = $('#social-reply-to').text();
        messaging_ajax($('#inbox-reply-message-full a').attr('href'), '#inbox-reply-message-full', 'html', true);
    }
});
