from django.urls import path
from making_queries.views import AuthorAPIViewDetails, EntryAPIViewDetails, BlogAPIViewDetails



urlpatterns = [
    path('', AuthorAPIViewDetails.as_view(), name="author-api-view-details"),
    path('entry/', EntryAPIViewDetails.as_view(), name="entry-api-view-details"),
    path('blog/', BlogAPIViewDetails.as_view(), name="blog-api-view-details"),


    
]