from django.shortcuts import render_to_response
from django.template import RequestContext

from markitup import settings
from markitup.markup import filter_func
from markitup.sanitize import sanitize_html

def apply_filter(request):
    cleaned_data = sanitize_html(request.POST.get('data', ''), strip=True)
    markup = filter_func(cleaned_data)
    return render_to_response( 'markitup/preview.html',
                              {'preview': markup},
                              context_instance=RequestContext(request))
