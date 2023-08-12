from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request,profiles,result):
    page = request.GET.get('page')
    paginator = Paginator(profiles, result)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndext = (int(page) + 2)
    if rightIndext > paginator.num_pages:
        rightIndext = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndext)
    return custom_range,profiles


def searchProfiles(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills))

    return profiles, search_query
