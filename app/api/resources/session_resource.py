from tastypie.resources import ModelResource
from tastypie.models import ApiKey
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie import fields

#from core.models import Session


class PublicSessionResource(ModelResource):
    """
    Public resource for session creation.
    
    In order to access her data,
    a user should create a session using
    basic authentication.
    
    Then using the api_key returned as part
    of the session she will be authorized
    to access other respurces. (token auth)
    
    TODO: Timed token invalidation.
    """
    
    user = fields.ToOneField('api.resources.UserResource', 'user', full=True)

    class Meta(object):
        queryset = ApiKey.objects.all()
        resource_name = 'sessions'
        fields = ['user', 'key', 'id']
        allowed_methods = ['post', 'get']
        authorization = Authorization()
        authentication = BasicAuthentication()
        always_return_data = True
        resource_uri_fieldname = 'token'

    def obj_create(self, bundle, request=None, **kwargs):
        """
        Create a new session
        """

        self.is_valid(bundle, request=request)
        bundle.obj = ApiKey.objects.create(user=request.user)
        return bundle

    #def dehydrate_resource_uri(self, bundle):
    #    return SessionResource().get_resource_uri(bundle.obj)


class SessionResource(ModelResource):

    user = fields.ToOneField('api.resources.UserResource', 'user', full=True)
    
    class Meta(object):
        queryset = ApiKey.objects.all()
        resource_name = 'sessions'
        fields = ['user', 'token']
        allowed_methods = ['get', 'delete']
        authorization = Authorization()
        #authentication = ApiTokenAuthentication()
        always_return_data = True
        resource_uri_fieldname = 'token'
