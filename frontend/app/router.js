import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('landing', {path: '/landing'});
  this.route('dataset_test');
  this.resource('users', function() {
    this.resource('user', { path: '/:user_id' });
  });

  this.route('dashboard', {path: '/'});
});

export default Router;
