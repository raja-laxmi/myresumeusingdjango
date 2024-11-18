from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

resume=[
    {
        'id':1,
        'title':'10th school',
        'education':'I COMPLETED MY 10TH IN STATEBOARD OF TELANGANA SSC UNDER KRISHNAVENNI HIGH SCHOOL  IN THE YEAR OF 2019 WITH CUMULATIVE GRADES PIONTS AVERAGE (8.5) GRADE `A`  ',
    },
    {
        'id':2,
        'title':'INTER',
        'education':'I COMPLETED MY 11TH AND 12TH  IN SRIGETHANJALI JUNIOUR COLLEGE IN THE YEAR OF 2021 WITH MARKS OF 800 IN THE BRANCH OF MEC(MATHEMATIS,ECONOMICS AND COMMERCE) ',
    },
    {
        'id':3,
        'title':'DEGREE COLLEGE',
        'education':'I GRADUATED IN THE YEAR OF 2024 IN ACME DEGREE COLLEGE AS A BACHLORS OF COMPUTER APPLICATION WITH AVERAGE PERCENTAGE OF  77.9% WITHOUT ANY BACKLOGS  AND I PARTICIPATTED MANY IDEATHONS AND HACKTHONS',
        
    },
    {
    'id':4,
    'title':'skill',
    'education':"'python','weddevelopment','mongodb','cisco cybersecurity','aspire leadership',i completed basic to advance python in online course such as coursela and completed mongodb in geeks for geeks,cisco cybersecurity in cisco academy and aspire leadership program in aspire education portal and currently learnning python fullstack in qspider"
    },
    {
        'id':5,
        'title':'achivements',
        'education':'i developed clone of netflix and got certificated by geeks for geeks in mongodb course and got badges from cisco cybersecurity course . and got certificate in aspire leadership program'
    }
]
def myresumeapps(request,id):
    
    data=None
    for i in resume:
        if i['id']==id:
            data=i

    context={
        'title':'alldata',
        'data':data,
    }
    return render(request,'pages/alldata.html',context)
def home (request):

    context= {
        'title':'home',
        'resume':resume,

    }
    return render(request,'pages/home.html',context)
def contact(request):
    context={
        'title':'contact'
    }
    return render(request,'pages/contact.html',context)
def about(request):
    about_data=[
        {
           'stream':"BACHLORS OF COMPUTER APPLICATION ",
           'score':'COMPLETED BCA WITH PERCENTAGE OF 79.8% IN THE YEAR OF 2024',
           'institute':"I COMPLETED MY BACHLOR'S DEGREE IN ACME DEGREE COLLEGE",
        },
        {
            'stream':'INTERMEDIATE',
            'score':'I COMPLETED MY INTERMEDIATE IN THE YEAR OF 2021 IN THE STREAM OF MEC(MATHEMATICS ECONOMICS COMMERCE) WITH MARKS OF 800',
            'institute':"I COMPLETED MY INTER IN THE SRI GEETAJALI JUNIOUR COLLEGE ",
        },
        {
            'stream':'10th',
            'score':"I COMPLETED MY TENTH IN 2019 WITH THE PERCENTAGE OF 8.5%",
            'institue':"I COMPLETED MY TENTH IN KRISHNAVENNI HIGH SCHOOL"
        }
    ]
    
    hard_skill=['python','SQL','HTML','CSS','JAVASCRIPT','CISCOCYBERSECURITY','ASPIRE LEADERSHIP','MONGODB']
    soft_skill=['OBSERVATION','DECISION MAKING','COMMMUNICATION','MULTI-TASKING']
    achievements_ofme=[
        {
            'acheive':'EDUNET FOUNDATION FULL STACK ',
            'create':" I LEARNT FRONTEND AND BOOTSTRAP IN THIS COURSES AND USED MY AMAZON CLOUD FOR FRONTEND ",
            'year':'2023',
        },
        {
            'acheive':'CISCO CYBERSECURITY ',
            'create':"EARNED CYBERSECURITY BADGES IN CISCO CYBERSECURITY ",
            'year':'2024',
        },
        {
            'acheive':'MONGODB',
            'create':"I COMPLETED MY MONGODB IN GEEKS FOR GEEKS AND CERTIFIATED",
            'year':'2024',
        },
        {
            'acheive':'PERSONAL PROTFOLIO',
            'create':"'A front-end personal portfolio site showcasing web development skills, with a modern, responsive design. Built using HTML, CSS, and JavaScript, it features an introduction, project showcase with interactive previews, and a contact form. '",
            'year':"2024",

        },
        {
            'acheive':'ASPIRE LEADERSHIP ',
            'create':"ASPIRE LEADERSHIP PROGRAM IS A PROGRAM WHICH TEST THE QUALITY OF LEADER ",
            'year':"2024",
        }
    ]

    context={
        'tilte':'about',
        'about_data':about_data,
        'hard_skill':hard_skill,
        'soft_skill':soft_skill,
        'achievements_ofme':achievements_ofme,

    }
    return render(request,'pages/about.html',context)