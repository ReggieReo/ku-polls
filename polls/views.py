from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Question, Choice, Vote


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, pk):
        """
        Return get request from the user. If the requested question does not
        exist or published redirect to index page.
        """
        this_user = request.user

        try:
            selected_question = get_object_or_404(Question, pk=pk)
        except Http404:
            messages.error(request, "The Question does not exist.")
            return HttpResponseRedirect(reverse("polls:index"))

        # make select_choice variable for showing previous selected choice
        if not this_user.is_authenticated:
            select_choice = ""
        else:
            try:
                # find a vote for this user
                vote = Vote.objects.get(
                    user=this_user, choice__question=selected_question
                )
                # set previous selected choice
                select_choice = vote.choice
            except Vote.DoesNotExist:
                # if user has not selected any choice set to empty string
                select_choice = ""

        if not (selected_question.is_published() or selected_question.can_vote()):
            messages.error(request, "The Question is not published yet.")
            return HttpResponseRedirect(reverse("polls:index"))
        else:
            return render(
                request,
                self.template_name,
                {
                    "question": selected_question,
                    "select_choice": select_choice,
                },
            )


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


@login_required
def vote(request, question_id):
    """
    Add vote count to voted choice, and show error message to user if user
    doesn't select any choice.
    """
    question = get_object_or_404(Question, pk=question_id)

    if not question.can_vote():
        messages.error(request, "The Question is not published yet.")
        return HttpResponseRedirect(reverse("polls:index"))

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    this_user = request.user
    try:
        # find a vote for this user
        vote = Vote.objects.get(user=this_user, choice__question=question)
        # update his vote
        vote.choice = selected_choice
    except Vote.DoesNotExist:
        # no matching vote -- create a new vote
        vote = Vote(user=this_user, choice=selected_choice)

    vote.save()
    # TODO: Use messages to display a confirmation on the results page.

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
