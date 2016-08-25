from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from gigaplan import Megaplan
import json
from django.conf import settings


def index_view(request):
    html = '<html><body><h1>Megaplan API Gateway.</h1> Any questions? Please contact suv at infotelekom.ru.</body>' \
           + '</html>'
    return HttpResponse(html)


@csrf_exempt
def create_client_contact_deal(request):
    def check_megaplan_response(data):
        if data['status']['code'] != 'ok':
            HttpResponse(json.dumps(data))
        return data

    if request.method != 'POST':
        return HttpResponseForbidden('Sorry, POST Only')

    key = request.GET.get('key', default=None)
    if key != settings.API_AUTH_KEY:
        return HttpResponseForbidden('403 Forbidden')

    data = json.loads(request.body.decode('utf-8'))

    print(request.body.decode('utf-8'))

    mega = Megaplan(settings.MEGAPLAN_HOSTNAME, settings.MEGAPLAN_USERNAME, settings.MEGAPLAN_PASSWORD)

    company = check_megaplan_response(mega.clients.add_company(name=data['orgName'],
                                                               phones=data['phones'].replace(' ', '').split(','),
                                                               responsible_ids=(data['manager2'],),
                                                               website=data['site']))

    payer = check_megaplan_response(mega.payers.edit(payer_id=company['data']['contractor']['PayerId'],
                                                     contractor_id=company['data']['contractor']['Id'],
                                                     address=', '.join((data['city'], data['address']))))

    person = check_megaplan_response(mega.clients.add_human(last_name=data['contactLastName'],
                                                            first_name=data['contactFirstName'],
                                                            middle_name=data['contactMiddleName'],
                                                            email=data['email'],
                                                            parent_company=company['data']['contractor']['Id'],
                                                            responsible_ids=(data['manager2'],),
                                                            phones=data['contactPhone'].replace(' ', '').split(',')))

    deal = check_megaplan_response(mega.deals.create(program_id=settings.MEGAPLAN_DEAL_PROGRAM_ID,
                                                     contractor_id=company['data']['contractor']['Id'],
                                                     contact_id=person['data']['contractor']['Id'],
                                                     manager_id=data['manager2'],
                                                     auditor_ids=(data['auditors'].split(',')),
                                                     operator_id=int(data['manager1'])))

    comment = check_megaplan_response(mega.comments.add(subject_type='deal', subject_id=deal['data']['deal']['Id'],
                                                        text=request.body.decode('utf-8')))

    if data['comment']:
        comment = check_megaplan_response(mega.comments.add(subject_type='deal', subject_id=deal['data']['deal']['Id'],
                                                          text=data['comment']))
    return HttpResponse(
        'https://' + settings.MEGAPLAN_HOSTNAME + '/deals/' + str(deal['data']['deal']['Id']) + '/card/',
        content_type='text/plain')
