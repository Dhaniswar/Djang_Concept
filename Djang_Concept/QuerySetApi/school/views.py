
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Teacher
from .serializers import  TeacherSerializer


# class StudentDetails(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']

#     def list(self, request):
#         print(" inside viewset")

#         serializer = StudentSerializer(many=True, context={'request': request,'hidden_fields': ['name', "roll", "city", "marks","pass_date"]})

#         return Response(serializer.data)


class TeacherDetails(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
























    '''QUERYSET API METHOD Those returns QuerySet'''
    """
    queryset = Student.objects.all() #all() return the object of all fields in the form of copy of current Queryset
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("Return => ", queryset)
    print("Behind  the scenes in SQL QUERY => ", queryset.query)
    print("*******************************SQL Query Query set Working in Django******************************************")
    queryset_filter = Student.objects.filter(name="Ankur") # filter return the maching lookup of querryset
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("Return => ", queryset_filter)
    print("Behind  the scenes in SQL QUERY => ", queryset_filter.query)
    print("*******************************SQL Query Query set Working in Django******************************************")
    queryset_exclude = Student.objects.exclude(name="Ankur") # filter return the maching lookup of new querryset
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("Return => ", queryset_exclude)
    print("Behind  the scenes in SQL QUERY => ", queryset_exclude.query)# exclude return the not matching lookup of new queryset
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("*******************************SQL Query Query set Working in Django******************************************")
    """
    # order_by(*fields) - It orders the fields
    # bydefault- Ascending
    # (-field)- descending
    # ('?')- Randomly
    """
    queryset_order_by = Student.objects.order_by("name") # order_by return the feilds in ascendding order
    print("Return Order Bydefault => ", queryset_order_by)
    print("Behind  the scenes in SQL QUERY => ", queryset_order_by.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    queryset_order_by = Student.objects.order_by("-name") # order_by return the feilds in descendding order when ('-field_name')
    print("Return in Descending Order=> ", queryset_order_by)
    print("Behind  the scenes in SQL QUERY => ", queryset_order_by.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    queryset_order_by = Student.objects.order_by("?") # order_by return the feilds in RANDOM order when ('?')
    print("Return => Randomly ", queryset_order_by)
    print("Behind  the scenes in SQL QUERY => ", queryset_order_by.query)# exclude return the not matching lookup of new queryset
    print("*******************************SQL Query Query set Working in Django******************************************")

    queryset_reverse = Student.objects.order_by("id").reverse()[:5] # This works only when there is ordering in queryset return last 5 records
    print("Return => Reverse ", queryset_reverse)
    print("Behind  the scenes in SQL QUERY => ", queryset_reverse.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    """
    # This return the list of dictionary rather than model instances
    # Each of those dictionaries represents an object, with the keys corresponding to the attributes names of model object
    """
    queryset_values = Student.objects.values("id") # This return the list of dictionary rather than model instances
    #queryset_values = Student.objects.values("id","city") # We can only display 2 columnn in table using values 
    print("Return => List of Dictionary ", queryset_values)
    print("Behind  the scenes in SQL QUERY => ", queryset_values.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    queryset_values_list = Student.objects.values_list() # This return all the tuple of dictionary rather than model instances
    #queryset_values = Student.objects.values("id","city") # We can only display 2 columnn in table using values 
    print("Return => Tuple of Dictionary ", queryset_values_list)
    print("Behind  the scenes in SQL QUERY => ", queryset_values_list.query)
    print("*******************************SQL Query Query set Working in Django******************************************")
    
    """
    # using(alias) method is for controlling which database the querySet will be evaluated against if ypu are using more than one database
    # This method takes only one parameter alias of databases
    """
    queryset_using = Student.objects.using("default") # This return all the tuple of dictionary rather than model instances
    print("Return => Default Databases ", queryset_using)
    print("Behind  the scenes in SQL QUERY => ", queryset_using.query)
    print("*******************************SQL Query Query set Working in Django******************************************")



    print("*******************************SQL Query Query set Working in Django******************************************")
    qs1 = Student.objects.values_list('id', 'city', named=True)
    qs2 = Teacher.objects.values_list('id', 'city', named=True)
    student_teacher = qs2.union(qs1, all=False)
    print("Return => Union ", student_teacher)
    print("Behind  the scenes in SQL QUERY => ", student_teacher.query)
    print("*******************************SQL Query Query set Working in Django******************************************")


    print("*******************************SQL Query Query set Working in Django******************************************")
    qs1 = Student.objects.values_list('name', named=True)
    qs2 = Teacher.objects.values_list('name', named=True)
    student_teacher = qs2.intersection(qs1)
    print("Return => Itersection ", student_teacher)
    print("Behind  the scenes in SQL QUERY => ", student_teacher.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    print("*******************************SQL Query Query set Working in Django******************************************")
    qs1 = Student.objects.values_list('name', named=True)
    qs2 = Teacher.objects.values_list('name', named=True)
    student_teacher = qs2.difference(qs1)
    print("Return => Difference ", student_teacher)
    print("Behind  the scenes in SQL QUERY => ", student_teacher.query)
    print("*******************************SQL Query Query set Working in Django******************************************")

    print("*******************************SQL Query Query set Working in Django******************************************")
    queryset = Student.objects.filter(Q(name="Naresh") & Q(roll=15))
    queryset = Student.objects.filter(~Q(name="Naresh"))
    print("Return => AND Operatotr Q ", queryset)
    print("Behind  the scenes in SQL QUERY => ", queryset.query)
    print("*******************************SQL Query Query set Working in Django******************************************")


    """
    


    '''QUERYSET API METHOD Those do not returns QuerySet'''
    """
    get() method retrive a single record.
    If there is no result match it will raise DoesNotExist exception
    if more than one item matches the get() query. It will raise MultipleObjectsReturned
    
    """
    """
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_get = Student.objects.get(pk=1) # get() method retrive a single record
    print("Return => Get Method ", student_get)
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_first = Student.objects.order_by('name').first() # first() method return the first model instance by default order by pk
    print("Return => first Method ", student_first)
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_last = Student.objects.order_by('name').last() # last() method return the last model instance by default order by pk
    print("Return => last Method ", student_last)
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_latest = Student.objects.latest('name') # It return the lasest object in the table based on the given field
    print("Return => latest Method ", student_latest)
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_earliest = Student.objects.earliest('pass_date') # It return the earliest object in the table based on the given field
    print("Return => earliest Method ", student_earliest)
    print("*******************************SQL Query Query set Working in Django******************************************")
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_get = Student.objects.all() # It return true if the queryset contains any result, and false if not
    print(student_get.exists())
    print("*******************************SQL Query Query set Working in Django******************************************")
    
    """

    """
    create(**kwargs) - A convenience method for creating an object and saving bit all in one step
    print("*******************************SQL Query Query set Working in Django******************************************")
    s = Student(name="Min", roll=32, city="Kathmandu", marks=25, pass_date='2020-05-04') #create(**kwargs) - A convenience method for creating an object and saving bit all in one step
    # for i in range(5):
    #     s.save()
    # print("Return => latest Method ", s)
    print("*******************************SQL Query Query set Working in Django******************************************")

    print("*******************************SQL Query Query set Working in Django******************************************")
    
    # for i in range(5):
    #     Student.objects.create(name="Min", roll=32, city="Kathmandu", marks=25, pass_date='2020-05-04') #create(**kwargs) - A convenience method for creating an object and saving bit all in one step
    print("*******************************SQL Query Query set Working in Django******************************************")

    """
   
    """
     get_or_create(default=None, **kwargs)-
     1. A convenience method for looking up an object with the given kwargs, creating one if necessary.
     2. kwargs(may be empty if your model has defaults for all fields)
     3. It returns a tuple of (object, created), where object is the retrieved or created

    print("*******************************SQL Query Query set Working in Django******************************************")
    student_data= Student.objects.get_or_create(name="Min", roll=32, city="Kathmandu", marks=25, pass_date='2020-05-04') #create(**kwargs) - A convenience method for creating an object and saving bit all in one step
    print("Return => ",student_data)
    print(created)
    print("*******************************SQL Query Query set Working in Django******************************************")
    """

    """
    1. It return the number of row match
    2. Update query for the specific fields
    print("*******************************SQL Query Query set Working in Django******************************************")
    student_update= Student.objects.filter(id=1).update(name='Ram', marks=98) # It return the number of row match
    print("Return => ",student_update)
    print(student_update)
    print("*******************************SQL Query Query set Working in Django******************************************")
    
    """

    """
    1. update_or_create(default=None, **kwargs) - A convenience method for updating an object with the given kwargs, cerating a new one if necessary
    2. the default is a dictionary of (field, value) pairs used to update the object. The values in default can be callables.

    student_data, created = Student.objects.update_or_create(id=14, name='Kohli', defaults={'name':'Sameeer'})

    """

