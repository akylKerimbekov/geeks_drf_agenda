from rest_framework import serializers

from movie_app.models import Director, Movie, Review


class ReviewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']


class ReviewSerializer(serializers.ModelSerializer):
    movie = ReviewMovieSerializer()

    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director avg_rate reviews'.split()

    def get_avg_rate(self, movie):
        sum = 0
        count = 1
        for star in movie.reviews.all():
            sum += star.stars
            count += 1
        return sum / count


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()
    def get_movies_count(self, director):
        return len(director.movies.all())
