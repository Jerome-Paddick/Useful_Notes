Django
===

Interactive Shell

    python manage.py shell
    
    from asdf.models import asdfModel
    asdfModel.all()
    

Serializer -> mechanism for translating Fjango models into other formats

Viewsets -> class-based View



---

### APIViews

    class AsdfView(APIView):
        def get(self, request, *args, **kwargs)
            return Response({"data":request.function})
        def put():
            return Response(serialiser.data) 
        def post():
        def delete():
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    
- Requests passed to handlers will be REST Framework's Response instead of HttpResponse object


---

### Serializers

- Convert between primitive values and internal datatypes
- validate inputs
- Retrieve and set values from parent objects


    serializer.SerializerMethodField(method_name=None)
    
- gets its value by calling a method on the serializer class it's attached to
- method_name defaults to get_\<field-name>

    
    class AsdfSerializer(serializer.modelserialiser):
        asdf = serializers.SerializerMethodField()
        
        def get_asdf(self, obj)
            return (val + obj.value)
            
- method should accept single argument -> object being serialized
- will return

### PyTest

    pytest <App>
    pytest <App/tests/file> -k <testname>
    
[overview](https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file)