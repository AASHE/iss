# -*- coding: utf-8 -*-
from south.v2 import DataMigration


NEW_ORG_TYPES = ["Associate",
                 "Baccalaureate",
                 "Master",
                 "Doctoral/Research"]


class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName".
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.

        OrganizationType = orm.OrganizationType

        for org_type in NEW_ORG_TYPES:
            OrganizationType.objects.create(name=org_type,
                                            id=org_type)

    def backwards(self, orm):
        "Write your backwards methods here."

        OrganizationType = orm.OrganizationType

        for org_type in NEW_ORG_TYPES:
            try:
                OrganizationType.objects.get(id=org_type).delete()
            except OrganizationType.DoesNotExist:
                pass


    models = {
        'iss.membership': {
            'Meta': {'object_name': 'Membership'},
            'current_dues_amount': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_modified_date': ('django.db.models.fields.DateField', [], {}),
            'membership_directory_opt_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iss.Organization']", 'null': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iss.MembershipProduct']"}),
            'receives_membership_benefits': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'termination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'iss.membershipproduct': {
            'Meta': {'object_name': 'MembershipProduct'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'iss.organization': {
            'Meta': {'object_name': 'Organization'},
            'account_num': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'business_member_level': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'carnegie_class': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'class_profile': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'enrollment_fte': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exclude_from_website': ('django.db.models.fields.IntegerField', [], {}),
            'is_defunct': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_member': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'is_signatory': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'member_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'membersuite_account_num': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'membersuite_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'org_name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'org_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iss.OrganizationType']", 'null': 'True'}),
            'picklist_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pilot_participant': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'primary_email': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'salesforce_id': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '33', 'null': 'True', 'blank': 'True'}),
            'stars_participant_status': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'street2': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sustainability_website': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'iss.organizationtype': {
            'Meta': {'object_name': 'OrganizationType'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['iss']
    symmetrical = True
