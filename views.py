from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.conf import settings
from djangotailoring.views import TailoredDocView
from djangotailoring.project import getsubjectloader
from mynav.nav import main_nav, tasks_nav
from .steps import steps_nav

# Create your views here.

def by_user_view(request):
    return render(request, 'myusage/by_user.html', {
        "main_nav": main_nav(request.user, 'staff_view'),
        "tasks_nav": tasks_nav(request.user, 'usage'),
        "steps_nav": steps_nav(request.user, 'by_user')
    })

"""
class Usage_Stats_View(TemplateView):
    template_name='mycoach/usage_stats.html'
 
    def dispatch(self, request, *args, **kwargs):
        from django.db.models import Count, Avg, Q # import the aggregators of interest
        # psudo constructor
        #Log_Request(request)
        configure_source_data(request.user.username)
        # load the nav object
        self.m_nav = StaffNav(request.path)

        Source1_students = Source1.objects.exclude(user_id='jtritz').exclude(user_id='mhuberth').exclude(user_id='tamckay').exclude(user_id='amymoors').exclude(user_id='no_data').exclude(user_id='jaredtritz@gmail.com').exclude(user_id='katemiller1027@gmail.com').exclude(user_id='murdockw')
        User_students = User.objects.exclude(username='jtritz').exclude(username='mhuberth').exclude(username='tamckay').exclude(username='amymoors').exclude(username='no_data').exclude(username='jaredtritz@gmail.com').exclude(username='katemiller1027@gmail.com').exclude(username='murdockw')
        ELog_students = ELog.objects.values('what').exclude(who='jtritz').exclude(who='mhuberth').exclude(who='tamckay').exclude(who='amymoors').exclude(who='jaredtritz@gmail.com').exclude(who='katemiller1027@gmail.com').exclude(who='murdockw')

        self.m_surveys_completed = len(Source1_students.filter(First_Survey_Complete="Yes"))
        self.m_surveys_incomplete = len(User_students.filter(elog__what__contains="Survey").annotate(ecnt=Count('elog__what', distinct=True)).annotate(scnt=Count('survey_log__id', distinct=True)).filter(scnt__lt=1))
        self.m_surveys_not_started = len(User_students.exclude(elog__what__contains="Survey").distinct('username'))

        #self.m_memorize_personal = len(Source1_students.filter(Q(Memorize_personal="Strongly_Agree") | Q(Memorize_personal="Agree")))
        self.m_memorize_personal = len(Source1_students.filter((Q(Memorize_personal="Strongly_Agree") | Q(Memorize_personal="Agree")) & Q(First_Survey_Complete="Yes")))
        self.m_math_confidence = len(Source1_students.filter((Q(Math_Confidence="Strongly_Agree") | Q(Math_Confidence="Agree")) & Q(First_Survey_Complete="Yes")))
        self.m_trust_calc = len(Source1_students.filter((Q(Trust_Calculation="Strongly_Agree") | Q(Trust_Calculation="Agree")) & Q(First_Survey_Complete="Yes")))
        self.m_hard_work_solve = len(Source1_students.filter((Q(Hard_work_personal_cant_solve="Strongly_Disagree") | Q(Hard_work_personal_cant_solve="Disagree")) & Q(First_Survey_Complete="Yes")))
        self.m_innate = len(Source1_students.filter((Q(Innate="Strongly_Disagree") | Q(Innate="Disagree")) & Q(First_Survey_Complete="Yes")))
        self.m_memorize_general = len(Source1_students.filter((Q(Memorize_general="Strongly_Agree") | Q(Memorize_general="Agree")) & Q(First_Survey_Complete="Yes")))
        self.m_recall_formula = len(Source1_students.filter((Q(Recall_Formula="Strongly_Agree") | Q(Recall_Formula="Agree")) & Q(First_Survey_Complete="Yes")))
        self.m_apply_principles = len(Source1_students.filter((Q(Apply_Principles="Strongly_Disgree") | Q(Apply_Principles="Disagree")) & Q(First_Survey_Complete="Yes")))
        self.m_hard_work_understand = len(Source1_students.filter((Q(Hard_work_personal_understand="Strongly_Disgree") | Q(Hard_work_personal_understand="Disagree")) & Q(First_Survey_Complete="Yes")))

        self.m_slc_interest = len(Source1_students.filter(Q(SLC_Interest="Signed_Up") | Q(SLC_Interest="Yes_Not_Signed_Up")))

        self.m_clicks_student = ELog_students.values('who').exclude(what__contains="Survey").annotate(wcnt=Count('who')).order_by('-wcnt')

        self.m_clicks_page = ELog_students.values('what').exclude(what__contains="Survey").annotate(wcnt=Count('what')).order_by('-wcnt')  

        return super(Usage_Stats_View, self).dispatch(request, *args, **kwargs)

    #over ride context creation for the template
    def get_context_data(self, **kwargs):
        context = super(Usage_Stats_View, self).get_context_data(**kwargs)
        context["nav"] = self.m_nav

        #context["surveys"] = dict({'completed140': 20})
        context["surveys"] = Source1.objects.survey_breakdown()

        #context["surveys_completed"] = self.m_surveys_completed
        context["surveys_completed"] = Source1.objects.with_surveys()
        context["surveys_incomplete"] = self.m_surveys_incomplete
        context["surveys_not_started"] = self.m_surveys_not_started

        context["memorize_personal"] = self.m_memorize_personal
        context["math_confidence"] = self.m_math_confidence
        context["trust_calc"] = self.m_trust_calc
        context["hard_work_solve"] = self.m_hard_work_solve
        context["innate"] = self.m_innate
        context["memorize_general"] = self.m_memorize_general
        context["recall_formula"] = self.m_recall_formula
        context["apply_principles"] = self.m_apply_principles
        context["hard_work_understand"] = self.m_hard_work_understand

        context["slc_interest"] = self.m_slc_interest

        context["clicks_student"] = self.m_clicks_student

        context["clicks_page"] = self.m_clicks_page
        return context


"""
