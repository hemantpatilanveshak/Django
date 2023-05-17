from django.shortcuts import render
from gamesapi.models import Games
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class GameDetails(APIView):

    def get(self,request,id=None):
        try:
            if id is not None:
                obj = Games.objects.get(id=id)
                # Game_Name = request.data.get('Game_Name')
                # Price = request.data.get('Price')
                # Ratings = request.data.get('Ratings')
                # Year_Of_Release = request.data.get('Year_Of_Release')

                data = {"Game_Name" : obj.Game_Name,"Price":obj.Price ,
                        "Ratings" : obj.Ratings, "Year_Of_Release" :obj.Year_Of_Release}
            
                return Response({"Msg":"Fetched Id Game","data":data})
            else:
                game = Games.objects.all()
                data = [{'id':obj.id, 'Game_Name':obj.Game_Name, 'Price':obj.Price ,
                         'Ratings' : obj.Ratings,'Year_Of_Release':obj.Year_Of_Release}
                        for obj in game]
                
                return Response({"data":data})
            
        except Games.DoesNotExist:
            return Response({"Message":"Game Id Does Not Exists"})
        


    def post(self,request):
        Game_Name = request.data.get('Game_Name',None)
        Price = request.data.get('Price',None)
        Ratings = request.data.get('Ratings',None)
        Year_Of_Release = request.data.get('Year_Of_Release',None)

        obj = Games.objects.create(Game_Name=Game_Name, Price= Price, 
                                   Ratings= Ratings,Year_Of_Release= Year_Of_Release)
        data = {"Game_Name" : obj.Game_Name,"Price":obj.Price ,
                "Ratings" : obj.Ratings, "Year_Of_Release" :obj.Year_Of_Release}
        
        return Response({"message": "Got some data!", "data": data })
    

    def put(self,request,id):
        try:
            obj = Games.objects.get(xy=id)
        except Games.DoesNotExist:
            return Response({"Message":"Game ID Does not exists"})

        Game_Name = request.data.get('Game_Name')
        Price = request.data.get('Price')
        Ratings = request.data.get('Ratings')
        Year_Of_Release = request.data.get('Year_Of_Release')

        obj.Game_Name = Game_Name
        obj.Price = Price
        obj.Ratings = Ratings
        obj.Year_Of_Release = Year_Of_Release

        obj.save()

        data = {"Game_Name" : obj.Game_Name,"Price":obj.Price ,"Ratings" : obj.Ratings, 
                "Year_Of_Release" :obj.Year_Of_Release}


        return Response({"msg":"Data Updated Successfully","data":data}) 


    def patch(self,request,id):
        try:
            obj = Games.objects.get(pk=id)
        except Games.DoesNotExist:
            return Response({"msg":"Id does not exists"})

        Game_Name = request.data.get('Game_Name')
        Price = request.data.get('Price')
        Ratings = request.data.get('Ratings')   
        Year_Of_Release = request.data.get('Year_Of_Release')

        if Game_Name:
            obj.Game_Name = Game_Name
        elif Price:
            obj.Price = Price
        elif Ratings:
            obj.Ratings = Year_Of_Release
        elif Year_Of_Release:
            obj.Year_Of_Release = Year_Of_Release

        
        obj.save()

        data = {"Game_Name" : obj.Game_Name,"Price":obj.Price ,
                "Ratings" : obj.Ratings, "Year_Of_Release" :obj.Year_Of_Release}

        return Response({"Msg":"Patch Data Confirm","data":data})       


    def delete(self,request,id):
        try:
            obj = Games.objects.get(id=id)
        except Games.DoesNotExist:
            return Response({"Message":"Game Id Does not exists"})
        

        obj.delete()
        return Response({"Message":"Data Deleted"})
