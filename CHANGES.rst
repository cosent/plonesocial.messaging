Changelog
=========

0.7.0 (unreleased)
------------------

* "Berlin" sprint

Completed
- @@social-inbox view (both the small and large views)
- Components added to the ploneintranet theme

Almost done
- Reply to a message has been added to the foot of a message conversation on @@social-inbox, but does not fully work just yet. It uses the tag and user buttons which we use on the activity stream.

To Do
- Bogdan is working on the BrowserView and template for the @@messaging-send form, Adrian has added this component for this to Plone Intranet Theme. You can find this under /demo/direct-message.html
- We need to talk about security at some point, as an Authenticated security check needs to be added to Plone Social at all levels (I guess)? It is certainly required for plone.social.messaging.
- The Patterns Lib component pat-tooltip only handles on success calls. Currently if the user is not logged in, then an unauthorised error is raised. I guess this should be handled by this pattern?
- The @@messaging-send should handle POSTs nicely. This is needed for the modal box and the reply field on @@social-inbox.
- We need to trigger the @@delete-message BrowserView element at some point


Earlier
-------

* Backend contributed, no changelog
