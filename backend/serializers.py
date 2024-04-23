from rest_framework import serializers

from backend.models import User, Vacancies, Skill, Experience


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации пользователей."""
    repeat_password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'repeat_password',
            'last_name',
            'email',
            'phone',
            'role'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        try:
            password, repeat_password = attrs.get(
                ('password', None), attrs.pop('repeat_password', None)
            )
        except ValueError:
            return f'Ошибка в поле {repeat_password}'

        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор профиля."""
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'description',
            'resume_file',
            'role'
        )


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор умений."""
    class Meta:
        model = Skill
        fields = ('title',)


class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = '__all__'


class VacanciesSerializer(serializers.ModelSerializer):
    """Сериализатор вакансий."""
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancies
        fields = '__all__'
