from rest_framework.views import APIView
from rest_framework.response import Response
from .serialize import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated

class testview(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,*ars, **kwargs):

        # data={"name": "faisal",
        #       "age": 25,"phone number": 8429454692,"adress":"sahab ganj station road",
        #       }
        post = Post.objects.all()
        serialize = PostSerializer(post, many=True)
        # serialize = PostSerializer()

        return Response(serialize.data)


    def post(self,request,*args,**kwargs):
        serialize=PostSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors)



