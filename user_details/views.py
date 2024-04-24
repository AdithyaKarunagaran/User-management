from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

# Create your views here.
import json
from user_details.models import Registermodel, AddressDetails, ContactDetails, VendorDtails


@csrf_exempt
@api_view(['POST', 'GET'])
def register(request):
    if request.method == "POST":
        b = json.loads(request.body)
        if 'id' not in b:
            obj = Registermodel.objects.create(
                firstname=b['firstname'],
                lastname=b['lastname'],
                userid=b['userid'],
                password=b['password'],
                mblenum=b['mblenum'],
                email=b['email'])
            a = [{'Message': 'Data Created'}]
            print(json.dumps(a))
            return JsonResponse(a, safe=False)
        else:
            obj = Registermodel.objects.filter(id=b['id']).update(
                firstname=b['firstname'],
                lastname=b['lastname'],
                userid=b['userid'],
                password=b['password'],
                mblenum=b['mblenum'],
                email=b['email'])
            a = [{'Message': 'Data Updated'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def address(request):
    if request.method == "POST":
        b = json.loads(request.body)
        if 'id' not in b:
            obj = AddressDetails.objects.create(
                line1=b['line1'],
                line2=b['line2'],
                pincode=b['pincode'],
                state=b['state'],
                city=b['city'],
                district=b['district'],
                created_by=b['created_by'])
            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj = AddressDetails.objects.filter(id=b['id']).update(
                line1=b['line1'],
                line2=b['line2'],
                pincode=b['pincode'],
                state=b['state'],
                city=b['city'],
                district=b['district'],
                created_by=b['created_by'])
            a = [{'Message': 'Data updated'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def contact(request):
    if request.method == "POST":
        b = json.loads(request.body)
        if 'id' not in b:
            obj = ContactDetails.objects.create(
                mobno=b['mobno'],
                emailid=b['emailid'],
                accountno=b['accountno'],
                beneficiaryname=b['beneficiaryname'],
                created_by=b['created_by'])
            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj = ContactDetails.objects.filter(id=b['id']).update(mobno=b['mobno'], emailid=b['emailid'],
                                                                   accountno=b['accountno'],
                                                                   beneficiaryname=b['beneficiaryname'],
                                                                   created_by=b['created_by'])
            a = [{'Message': 'Data Updated'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def vendor_models(request):
    if request.method == "POST":
        b = json.loads(request.body)
        if 'id' not in b:
            obj = VendorDtails.objects.create(
                name=b['name'],
                code=b['code'],
                gst=b['gst'],
                pan=b['pan'],
                branch=b['branch'],
                Address_Details_id=b['Address_Details'],
                Contact_Details_id=b['Contact_Details'],
                created_by=b['created_by'])
            a = [{'Message': 'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj = VendorDtails.objects.filter(id=b['id']).update(
                name=b['name'],
                code=b['code'],
                gst=b['gst'],
                pan=b['pan'],
                Address_Details_id=b['Address_Details'],
                Contact_Details_id=b['Contact_Details'],
                created_by=b['created_by'])
            a = [{'Message': 'Data Updated'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def get_register(request):
    if request.method == "GET":
        obj = Registermodel.objects.all()
        a = []

        for i in obj:
            b = {
                "Firstname": i.firstname,
                "Lastname": i.lastname
            }
            a.append(b)
        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def get_address(request):
    if request.method == "GET":
        obj = AddressDetails.objects.all()
        a = []

        for i in obj:
            b = {
                "line1": i.line1,
                "city": i.city,
                "district": i.district,
                "pincode": i.pincode
            }
            a.append(b)
        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def get_contact(request):
    if request.method == "GET":
        obj = ContactDetails.objects.all()
        a = []
        for i in obj:
            b = {
                "Mobile No": i.mobno,
                "Email Id": i.emailid,
            }
            a.append(b)
        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def get_vendor(request):
    if request.method == "GET":
        obj = VendorDtails.objects.all()
        a = []
        for i in obj:
            b = {
                "Vendor Name": i.name,
                "Vendor Code": i.code,
                "GST No": i.gst,
                "PAN No": i.pan,
                "Address": {"City": i.Address_Details.city, "District": i.Address_Details.district},
                "Contact": {"Mobile No": i.Contact_Details.mobno, "Email Id": i.Contact_Details.emailid}
            }
            a.append(b)
        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def reg_get(request, pk):
    if request.method == "GET":
        obj = Registermodel.objects.get(id=pk)

        a = {
            "name": obj.firstname,
            "lname": obj.lastname
        }

    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def add_get(request, pk):
    if request.method == "GET":
        obj = AddressDetails.objects.get(id=pk)

        a = {
            "Address 1": obj.line1,
            "Address 2": obj.line2
        }

    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def con_get(request, pk):
    if request.method == "GET":
        obj = ContactDetails.objects.get(id=pk)

        a = {
            "Mobile No": obj.mobno,
            "Email ID": obj.emailid
        }
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def vend_get(request, pk):
    if request.method == "GET":
        obj = VendorDtails.objects.get(id=pk)

        a = {
            "Name": obj.name,
            "Code": obj.code
        }
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def index_form(request):
    if request.method == "GET":
        pass
    return render(request, 'index.html')


@csrf_exempt
@api_view(['POST', 'GET'])
def reg_search(request):
    if request.method == "GET":
        b = request.GET.get('firstname')
        obj = Registermodel.objects.filter(firstname__icontains=b, lastname__icontains=b)
        a = []

        for i in obj:
            b = {
                "firstname": i.firstname,
                "lastname": i.lastname
            }
            a.append(b)
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST', 'GET'])
def add_search(request):
    if request.method == "GET":
        r1 = request.GET.get("city")
        r2 = request.GET.get("district")
        r3 = request.GET.get("id")
        query = Q()

        if r1:
            query |= Q(city__icontains=r1)
        if r2:
            query |= Q(district__icontains=r2)
        if r3:
            query |= Q(id__contains=r3)
        obj = AddressDetails.objects.filter(query)

        response_data = []
        for i in obj:
            data = {"ID": i.id, "City": i.city, "District": i.district}
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def con_search(request):
    if request.method == "GET":
        r1 = request.GET.get("ph")
        r2 = request.GET.get("email")
        r3 = request.GET.get("id")
        query = Q()

        if r1:
            query |= Q(mobno__icontains=r1)
        if r2:
            query |= Q(emailid__icontains=r2)
        if r3:
            query |= Q(id__icontains=r3)
        obj = ContactDetails.objects.filter(query)

        response_data = []
        for i in obj:
            data = {"ID": i.id, "Mobile NO": i.mobno, "Email": i.emailid}
            response_data.append(data)
        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST', 'GET'])
def vend_search(request):
    if request.method == "GET":
        r1 = request.GET.get("name")
        r2 = request.GET.get("code")
        r3 = request.GET.get("gst")
        r4 = request.GET.get("pan")
        r5 = request.GET.get("branch")
        r6 = request.GET.get("id")
        query = Q()

        if r1:
            query |= Q(name__icontains=r1)
        if r2:
            query |= Q(code__contains=r2)
        if r3:
            query |= Q(gst__icontains=r3)
        if r4:
            query |= Q(pan__icontains=r4)
        if r5:
            query |= Q(branch__icontains=r5)
        if r6:
            query |= Q(id__contains=r6)

        obj = VendorDtails.objects.filter(query)

        response_data = serialize('json', obj)
        return HttpResponse(response_data, content_type="application/json")


@csrf_exempt
@api_view(['DELETE'])
def delete_reg(request, pk):
    if request.method == "DELETE":
        _, deleted = Registermodel.objects.filter(id=pk).delete()
        if deleted:
            response_data = {"message": "Data successfully deleted"}
        else:
            response_data = {"message": "No data found to delete"}

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['DELETE'])
def delete_add(request, pk):
    if request.method == "DELETE":
        _, deleted = AddressDetails.objects.filter(id=pk).delete()
        if deleted:
            response_data = {"message": "Data successfully deleted"}
        else:
            response_data = {"message": "No data found to delete"}

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['DELETE'])
def delete_con(request, pk):
    if request.method == "DELETE":
        _, deleted = ContactDetails.objects.filter(id=pk).delete()
        if deleted:
            response_data = {"message": "Data successfully deleted"}
        else:
            response_data = {"message": "No data found to delete"}

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['DELETE'])
def delete_vend(request, pk):
    if request.method == "DELETE":
        _, deleted = VendorDtails.objects.filter(id=pk).delete()
        if deleted:
            response_data = {"message": "Data successfully deleted"}
        else:
            response_data = {"message": "No data found to delete"}

        return HttpResponse(json.dumps(response_data))


@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        obj = Registermodel.objects.filter(userid=data["userid"], password=data["password"])

        if not obj.exists():
            response_data = [{"message": "failed"}]

        else:
            response_data = [{"message": "success"}]
        print(json.dumps(response_data))
        return JsonResponse(response_data, safe=False)