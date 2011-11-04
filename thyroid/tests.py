from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from thyroid.models import Diagnosis

import logging

class DiagnosisListTests(TestCase):
    fixtures = ['diagnosis_list',]

    def setUp(self):
        self.diagnosis = Diagnosis.objects.order_by('category__order')
        self.url = reverse('thy_diagnosis_list')
        self.client = Client()

    def test_variable(self):
        response = self.client.get(self.url)
        for d in response.context['diagnoses']:
            self.assertTrue(d in self.diagnosis)
        for d in self.diagnosis:
            self.assertTrue(d in response.context['diagnoses'])

    def test_get_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
            'thyroid/diagnosis_list.html')
