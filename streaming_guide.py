# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: December 8th, 2023
# Description: This program defines classes to represent movies, streaming services, and a guide to find where movies are streaming.

class Movie:
    """Represent a movie with a title, genre, director, and release year."""
    def __init__(self, title, genre, director, year):
        """Initialize a new Movie instance."""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Return the title of the movie."""
        return self._title

    def get_genre(self):
        """Return the genre of the movie."""
        return self._genre

    def get_director(self):
        """Return the director of the movie."""
        return self._director

    def get_year(self):
        """Return the release year of the movie."""
        return self._year

class StreamingService:
    """Represent a streaming service with a name and a catalog of movies."""
    def __init__(self, name):
        """Initialize a new StreamingService instance."""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Return the name of the streaming service."""
        return self._name

    def get_catalog(self):
        """Return the catalog of movies."""
        return self._catalog

    def add_movie(self, movie):
        """Add a movie to the streaming service's catalog."""
        self._catalog[movie.get_title()] = movie

    def delete_movie(self, title):
        """Remove a movie from the streaming service's catalog."""
        if title in self._catalog:
            del self._catalog[title]

class StreamingGuide:
    """Represent a guide to find where movies are streaming."""
    def __init__(self):
        """Initialize a new StreamingGuide instance."""
        self._streaming_services = []

    def add_streaming_service(self, service):
        """Add a streaming service to the guide."""
        self._streaming_services.append(service)

    def delete_streaming_service(self, name):
        """Remove a streaming service from the guide."""
        self._streaming_services = [s for s in self._streaming_services if s.get_name() != name]

    def where_to_watch(self, title):
        """Return a list of streaming services where the movie is available."""
        services_with_movie = [service.get_name() for service in self._streaming_services if title in service.get_catalog()]
        if not services_with_movie:
            return None
        movie_year = self._streaming_services[0].get_catalog()[title].get_year()
        return [f"{title} ({movie_year})"] + services_with_movie


