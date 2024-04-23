from django.contrib import admin

from backend.models import User, Experience, Vacancies, Skill


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'start_date',
        'end_date',
        'expected_salary',
        'user',
        'slug'
    )
    list_display_links = (
        'id', 'title'
    )
    search_fields = (
        'title', 'user__username'
    )


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'salary_min',
        'salary_max',
        'user',
        'slug'
    )
    list_display_links = (
        'id', 'title'
    )
    search_fields = (
        'title', 'user__username'
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'slug'
    )


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'phone',
        'role',
        'slug'
    )
    list_display_links = (
        'id',
        'username',
        'email',
        'phone'
    )
    search_fields = (
        'username',
    )
    list_filter = ('role', )


admin.site.register(User, UsersAdmin)
