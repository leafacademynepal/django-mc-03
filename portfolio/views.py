from django.views.generic import TemplateView
from cv.models import Skill

# yeha hamle django le diyeko kunai pani html file open garna lai or server garna lai TemplateView use gareko ho
# IndexPageView -> yo function or class  call garne bitikai - index.html file open gar 

class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        #select * from skill
        data["skill_list"] = Skill.objects.all()
        return data
