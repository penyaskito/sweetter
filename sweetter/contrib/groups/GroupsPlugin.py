from django.template.loader import render_to_string
from sweetter.contrib.groups.models import Group

class GroupHooks:
    def __init__(self):
        pass
        
    def sidebar(self, context):
        if context['user'] and not context['user'].is_authenticated():
            return ''
        else:
            user = context['user']        
            return render_to_string('groupsidebar.html', {
                    'group_list': Group.objects.filter(users__user=user),
                }, context_instance=context)
    
    def tools(self, context, post):
        return ''
        
    def parse(self, value):
        return value