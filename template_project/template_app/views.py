from django.shortcuts import render , redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from . import forms

from . import models

from .consumer import notifiSeguim_lst_msg, notifiLikes_lst_msg, noticias_lst_msg
from .producer import msg_seguir_usuario, msg_like_post, msg_crear_post
from .newtopic import crear_topic_seguidores


def login_index(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
	# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = forms.LoginForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				
				username = request.POST['username']
				password = request.POST['password']
				
				user = authenticate(request, username=username, password=password)

				if user is not None:
						if user.is_active:				
							login(request, user)
							return redirect('home')
							messages.success(request,'Te has identificado correctamente.')
						else:
							messages.error(request,'Tu usuario no esta activo.')
				else:
					messages.error(request,'Usuario y/o contraseña incorrectas.')

				form = forms.LoginForm()
				context = {'form': form}
		else:

			form = forms.LoginForm()
			context = {'form': form}

	return render(request, 'index.html', context)


def logout_index(request):
	logout(request)
	return redirect('login')


def registrarse(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = forms.RegisterForm()
		if request.method == 'POST':
			form = forms.RegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,'Te has registrado con exito '+ user)
				msg = crear_topic_seguidores(user)
				print(msg)
				return redirect('login')
			else:
				messages.error(request,'Error al registrarte')

	context = {'form':form}

	return render(request, 'register.html', context)


@login_required(login_url='login')
def template_view(request):

	item_list = []

	context = {'item_list': item_list}

	return render(request, 'home.html', context)


@login_required(login_url='login')
def crearPost(request):

	item_list = []
	form_post = forms.CargarPost(request.POST, request.FILES) 

	if form_post.is_valid():
		titulo = form_post.cleaned_data['titulo']
		texto = form_post.cleaned_data['texto']
		autor = str(request.user)

		for f in request.FILES.getlist('imagen'): 
			models.Post.objects.create(autor= autor, titulo=titulo, imagen=f, text = texto)
		messages.success(request,'Post creado correctamente ')

		post = models.Post.objects.filter(autor= autor, titulo=titulo, text = texto)

		for p in post:
			idPost = p.id

		lst_topics = []

		lst_seguidores = models.Seguidos.objects.filter(seguido= autor)

		for item in lst_seguidores:
			lst_topics.append(item.seguidor+"_News")

		msg = msg_crear_post(str(idPost), lst_topics)
		print(msg)


		form_post = forms.CargarPost()
	else:
		item_list = []
		form_post = forms.CargarPost()

	context = {'item_list': item_list, 'form_post': form_post}

	return render(request, 'cargaPost.html', context)


@login_required(login_url='login')
def verNoticias(request):

	item_list = []
	lst_msg_generator_idPost_aux = []
	lst_msg_generator_idPost = []
	generator_idPost = noticias_lst_msg(str(request.user))

	for item in generator_idPost:				# EXTRAE CADA MJE DEL TOPIC Y LO GUARDA EN UNA LISTA
		for i in item:
			lst_msg_generator_idPost_aux.append(i)				
		
	for item in lst_msg_generator_idPost_aux[::-1]:			#INVIERTE EL ORDEN DE LA LISTA PARA QUE EL MJE MAS RECIENTE ESTE PRIMERO
		lst_msg_generator_idPost.append(item)
	print (lst_msg_generator_idPost)

	for item in lst_msg_generator_idPost:
		post = models.Post.objects.filter(id = int(item))

		for item in post: 
			item_list.append(item)

	form_msg = forms.ObtenerPost();
	
	if request.method == 'POST':
		form_msg = forms.ObtenerPost(request.POST)
		if form_msg.is_valid():
			autor = form_msg.cleaned_data['autor']
			titulo = form_msg.cleaned_data['titulo']
			texto = form_msg.cleaned_data['texto']
			post_lst = models.Post.objects.get(autor= autor, titulo=titulo, text = texto)
			
			models.Likes.objects.create(idPost= post_lst.id, seguidor=autor)
			msg = msg_like_post(str(request.user), post_lst.autor, post_lst.titulo)		# LLAMA A PRODUCER.PY
			print (msg)

		else:
			form_msg = forms.ObtenerPost()
	else:
		form_msg = forms.ObtenerPost()

	context = {'item_list': item_list, 'form_msg': form_msg}

	return render(request, 'verNoticias.html', context)



@login_required(login_url='login')
def buscarUsuarios(request):

	form_msg= forms.BuscarUsrForm()

	if request.method == 'POST':
		form_msg = forms.BuscarUsrForm(request.POST)
		if form_msg.is_valid():
			usuario = form_msg.cleaned_data['mensaje']
			autor = str(request.user)

			models.Seguidos.objects.create(seguidor= autor, seguido=str(usuario))
			msg = msg_seguir_usuario(autor, str(usuario))		# LLAMA A PRODUCTOR (PRODUCER.PY)

			print (msg)
			messages.success(request, autor + " sigue a "+ str(usuario))
			form_msg = forms.BuscarUsrForm()
		else:
			form_msg = forms.BuscarUsrForm()
	else:
		form_msg = forms.BuscarUsrForm()
	
	context = {'form_msg': form_msg }

	return render(request, 'buscarUsuarios.html', context)


@login_required(login_url='login')
def notificaciones(request):

	lst_msg_generator_seg_aux = []
	lst_msg_generator_seg = []

	lst_msg_generator_likes_aux = []
	lst_msg_generator_likes = []

	user = str(request.user)

	generator_seguidores = notifiSeguim_lst_msg(user)		# LLAMA A CONSUMIDOR (CONSUMER.PY)
	generator_likes = notifiLikes_lst_msg(user)				# LLAMA A CONSUMIDOR (CONSUMER.PY)

	for item in generator_seguidores:				# EXTRAE CADA MJE DEL TOPIC Y LO GUARDA EN UNA LISTA
		for i in item:
			lst_msg_generator_seg_aux.append(i)				
		
	for item in lst_msg_generator_seg_aux[::-1]:			#INVIERTE EL ORDEN DE LA LISTA PARA QUE EL MJE MAS RECIENTE ESTE PRIMERO
		lst_msg_generator_seg.append(item)
	print (lst_msg_generator_seg)

	for item in generator_likes:				# EXTRAE CADA MJE DEL TOPIC Y LO GUARDA EN UNA LISTA
		for i in item:
			lst_msg_generator_likes_aux.append(i)				
		
	for item in lst_msg_generator_likes_aux[::-1]:			#INVIERTE EL ORDEN DE LA LISTA PARA QUE EL MJE MAS RECIENTE ESTE PRIMERO
		lst_msg_generator_likes.append(item)
	print (lst_msg_generator_likes)


	context = {'item_list_seg': lst_msg_generator_seg, 'item_list_likes': lst_msg_generator_likes}

	return render(request, 'notificaciones.html', context)

