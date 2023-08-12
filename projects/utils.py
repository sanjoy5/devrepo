from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProjects(request,projects,result):
    page = request.GET.get('page')
    paginator = Paginator(projects, result)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 1)
    if leftIndex < 1:
        leftIndex = 1

    rightIndext = (int(page) + 2)
    if rightIndext > paginator.num_pages:
        rightIndext = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndext)

    return custom_range,projects


def searchProjects(request):

    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects, search_query
