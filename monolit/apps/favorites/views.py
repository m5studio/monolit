from django.shortcuts import render, redirect
from django.http import JsonResponse


def favorites_list(request):
    context = {}
    return render(request, 'favorites/favorites_list.html', context=context)


# def add_to_favorites(request, id):
def add_to_favorites(request):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])

        # check if item exist in list of dicts
        item_exist = next((item for item in request.session['favorites'] if item["type"] == request.POST.get('type') and item["id"] == request.POST.get('id')), False)

        # Get item request data
        add_data = {
            'type': request.POST.get('type'),
            'id': request.POST.get('id'),
        }

        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True

    # For AJAX requests
    if request.is_ajax():
        data = {
            'type': request.POST.get('type'),
            'id': request.POST.get('id'),
        }
        request.session.modified = True
        return JsonResponse(data)
    # END For AJAX requests
    return redirect(request.POST.get('url_from'))


# def remove_from_favorites(request, id):
def remove_from_favorites(request):
    if request.method == 'POST':
        # Delete an item from favorites
        for item in request.session['favorites']:
            if item['id'] == request.POST.get('id') and item['type'] == request.POST.get('type'):
                item.clear()

        # remove empty {} from favorites list
        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        # remove favorites if favorites list is empty
        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True

    # For AJAX requests
    if request.is_ajax():
        data = {
            'type': request.POST.get('type'),
            'id': request.POST.get('id'),
        }
        request.session.modified = True
        return JsonResponse(data)
    # END For AJAX requests
    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']
        # request.session.modified = True
    return redirect(request.POST.get('url_from'))


def favorites_api(request):
    return JsonResponse(request.session.get('favorites'), safe=False)
