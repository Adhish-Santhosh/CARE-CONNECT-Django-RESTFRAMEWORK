from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from Clinic.models import Doctor,AppointmentDb
from Clinic.serializers import DoctorSerializer,AppointmentSerializer
from datetime import datetime, time, timedelta

# Create your views here.


class DoctorListCreateView(APIView):
    def get(self,request):
        qs=Doctor.objects.all()
        serializer_instance=DoctorSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
class DoctorRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(Doctor,id=pk)
        serializer_instance=DoctorSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        Doctor_objects=get_object_or_404(Doctor,id=pk)


        serializer_instance=DoctorSerializer(data=form_data,instance=Doctor_objects)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        doctor_objects=get_object_or_404(Doctor,id=pk)
        doctor_objects.delete()
        return Response(data={"message":"deleted sucessfully... !"})
class AppointmentListCreateView(APIView):
    def get(self,request):
        qs=AppointmentDb.objects.all()
        serializer_instance=AppointmentSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=AppointmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            appointment_date=serializer_instance.validated_data.get("appointment_date")
            doctor_id=serializer_instance.validated_data.get("doctor_id")

            last_appointment = AppointmentDb.objects.filter(
                appointment_date=appointment_date,
                doctor_id=doctor_id
            ).order_by("-token_number").first()


            if last_appointment is None:
                form_data["token_number"]=1
                form_data["appointment_time"]=time(10,0)
            else:
                next_token=last_appointment.token_number+1
                current_time=datetime.combine(appointment_date,last_appointment.appointment_time)
                next_time=current_time+timedelta(minutes=15)

                form_data["token_number"]=next_token
                form_data["appointment_time"]=next_time
                if next_time.time() >= time(12, 30):
                     next_time = datetime.combine(appointment_date,time(13, 30))


            qs=AppointmentDb.objects.create(**form_data)
            serializer_instance=AppointmentSerializer(qs)
            return Response(data={
                "Message":"Booked Sucessfully",
                "Token Number is" : form_data["token_number"]
            })
        else:
             return Response(data=serializer_instance.errors)


            


