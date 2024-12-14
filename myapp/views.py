from django.shortcuts import render, redirect
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from django.http.response import JsonResponse
#from myapp.serializers import userSerializer
from django.shortcuts import render, redirect
from .models import UserProfile
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from django.http.response import JsonResponse
#from myapp.serializers import userSerializer
from django.shortcuts import render, redirect
from .models import UserProfile
from PIL import Image, ImageDraw, ImageFont


def dashboard(request):
    if request.method == 'POST':
        # Check if the user has a UserProfile object
        if hasattr(request.user, 'userprofile'):
            user_profile = request.user.userprofile
        else:
            # If not, create a new UserProfile object
            user_profile = UserProfile.objects.create(user=request.user)

        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            user_profile.profile_picture = profile_picture
        
        # Update bio and skills
        user_profile.bio = request.POST.get('bio', '')
        user_profile.skills = request.POST.get('skills', '')
        
        # Save the changes
        user_profile.save()
        print(user_profile.profile_picture.path)
        
        # Redirect to the dashboard or a success page
        return redirect('dashboard')

    else:
        # Render the dashboard template with the user's profile data
        return render(request, 'dashboard.html')



# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

#from rest_framework.decorators import api_view
#@api_view(http_method_names=['POST'])
from django.urls import reverse

# Other imports...

def register(request):
    print("Print 1")
    if request.method == 'POST':
        print("Print 2")
        print(request)
        username = request.POST['username']
        print(username)
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect(reverse('login'))
        else:
            messages.info(request, "Password not matched")
            return redirect('register')
    else:
        return render(request, 'register.html')

#@api_view(http_method_names=['POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1, 2, 3, 4, 5, 'adi', 'mad', 'pan']
    return render(request, 'counter.html', {'posts': posts} )

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def about(request):
    return render(request, 'about.html')

def tutorials(request):
    return render(request, 'tutorials.html')

def tutorials2(request):
    return render(request, 'tutorials2.html')

def tutorials3(request):
    return render(request, 'tutorials3.html')

def tutorials4(request):
    return render(request, 'tutorials4.html')

def tutorials5(request):
    return render(request, 'tutorials5.html')

def tutorials6(request):
    return render(request, 'tutorials6.html')

def community(request):
    return render(request, 'community.html')

def python(request):
    return render(request, 'python.html')

def django(request):
    return render(request, 'django.html')

def blog(request):
    return render(request, 'blog.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def quizes(request):
    return render(request, 'quizes.html')

def quizesdjango(request):
    return render(request, 'quizesdjango.html')

def quizesdjangob(request):
    return render(request, 'quizesdjangob.html')

def quizesapi(request):
    return render(request, 'quizesapi.html')

def quizescs50(request):
    return render(request, 'quizescs50.html')

def quizesscipy(request):
    return render(request, 'quizesscipy.html')

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CommunityMessage
from .forms import CommunityMessageForm

@login_required
def community(request):
    if request.method == 'POST':
        form = CommunityMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            form = CommunityMessageForm()  # Clear the form after submission
    else:
        
        form = CommunityMessageForm()

    messages = CommunityMessage.objects.all().order_by('-timestamp')
    return render(request, 'community.html', {'form': form, 'messages': messages})

# views.py (or wherever you handle the message submission)
def submit_community_message(request):
    # Get the current user
    user = request.user

    # Get the message from the form or request data
    message_text = request.POST.get('message', '')

    # Create a new CommunityMessage instance
    community_message = CommunityMessage(user=user, message=message_text)
    community_message.save()

    # ...
    

from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Create and save the message to the database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        return render(request, 'contact.html')  # Create a success page

    return render(request, 'contact.html')

# views.py
from django.http import FileResponse, HttpResponse
from PIL import Image, ImageDraw, ImageFont
import io

def generate_certificate(request):
    student_name = request.user.username  # Get the student's name from the login

    try:
        # Open the certificate image
        img = Image.open('E:\\Djangoback\\myproject\\static\\certificate2.jpeg')
    except FileNotFoundError:
        return HttpResponse('Certificate image not found.', status=404)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(img)

    # Specify the font, size, and color
    font = ImageFont.truetype('arial.ttf', 50)
    color = 'rgb(0, 0, 0)'  # black color

    # Specify the position where the student's name will be added
    position = (590, 435)  # This is just an example, adjust it as needed


    # Draw the text on the image
    draw.text(position, student_name, fill=color, font=font)

    # Save the image to a BytesIO object
    img_io = io.BytesIO()
    img.save(img_io, format='JPEG')
    img_io.seek(0)  # Go back to the start of the BytesIO object

    # Create a FileResponse with the BytesIO object
    response = FileResponse(img_io, content_type='image/jpeg')

    return response