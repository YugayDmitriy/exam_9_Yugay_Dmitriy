from django.shortcuts import render, get_object_or_404
import json
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Galapp import forms, models



def context_data():
    context = {
        'page_name': '',
        'page_title': '',
        'system_name': 'Фото Галерея',
        'topbar': True,
        'footer': True,
    }
    return context


@login_required
def upload_modal(request):
    context = context_data()
    return render(request, 'upload.html', context)


@login_required
def home(request):
    context = context_data()
    context['page'] = 'home'
    context['page_title'] = 'Home'
    context['uploads'] = models.Gallery.objects.filter(delete_flag=0, user=request.user).count()
    context['trash'] = models.Gallery.objects.filter(delete_flag=1, user=request.user).count()
    print(context)
    return render(request, 'home.html', context)


@login_required
def save_upload(request):
    resp = {'status': 'failed', 'msg': ''}
    if not request.method == 'POST':
        resp['msg'] = "No data has been sent on this request"
    else:
        form = forms.SaveUpload(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Изображение успешно сохранено.")
        resp['status'] = 'success'
    else:
        for field in form:
            for error in field.errors:
                if resp['msg'] != '':
                    resp['msg'] += str('<br />')
                resp['msg'] += str(f"[{field.name}] {error}.")
    return HttpResponse(json.dumps(resp), content_type="application/json")



@login_required
def view_gallery(request):
    context = context_data()
    context['page_title'] = "Gallery"
    context['photos'] = models.Gallery.objects.filter(user=request.user, delete_flag=0).all().order_by('-date_created')
    return render(request, 'gallery.html', context)


def favorite_photo(request, id):
    photo = get_object_or_404(models.Gallery, id=id)
    if photo.favorite.filter(id=request.user.id).exists():
        photo.favorite.remove(request.user)
    else:
        photo.favorite.add(request.user)
    return HttpResponseRedirect(photo.get_absolute_url())


@login_required
def view_trash(request):
    context = context_data()
    context['page_title'] = "Trashed Images"
    context['photos'] = models.Gallery.objects.filter(user=request.user, delete_flag=1).all()
    return render(request, 'trash.html', context)


@login_required
def trash_upload(request, pk=None):
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'No data sent in this request'
    else:
        try:
            upload = models.Gallery.objects.filter(id=pk).update(delete_flag=1)
            resp['status'] = 'success'
            messages.success(request, 'Изображение успешно добавлено в корзину')
        except:
            resp['msg'] = 'Invalid data to delete'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def restore_upload(request, pk=None):
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'No data sent in this request'
    else:
        try:
            upload = models.Gallery.objects.filter(id=pk).update(delete_flag=0)
            resp['status'] = 'success'
            messages.success(request, 'Изображение успешно восстановлено')
        except:
            resp['msg'] = 'Invalid data to delete'
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def delete_upload(request, pk=None):
    resp = {'status': 'failed', 'msg': ''}
    if pk is None:
        resp['msg'] = 'No data sent in this request'
    else:
        try:
            upload = models.Gallery.objects.get(id=pk).delete()
            resp['status'] = 'success'
            messages.success(request, 'Изображение успешно удалено навсегда')
        except:
            resp['msg'] = 'Invalid data to delete'
    return HttpResponse(json.dumps(resp), content_type="application/json")
