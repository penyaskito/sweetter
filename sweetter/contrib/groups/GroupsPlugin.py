from django.template.loader import render_to_string

from contrib.groups.models import Group
from ublogging.api import Plugin


class GroupHooks(Plugin):
    def sidebar(self, context):
        if not context.get('viewing_user','') and context['perms'].user and not context['perms'].user.is_authenticated():
            return ''
        else:
            if context.get('viewing_user', ''):
                user = context['viewing_user']
            else:
                user = context['perms'].user
            return render_to_string('groupsidebar.html', {
                    'group_list': Group.objects.filter(users__user=user),
                }, context_instance=context)
