import Ember from 'ember';
import Resolver from 'ember/resolver';
import loadInitializers from 'ember/load-initializers';
import config from './config/environment';
//import timeAgo from './helpers/time-ago';

Ember.Handlebars.registerBoundHelper('time-ago', function(date) {
  return moment(date).fromNow();
});
Ember.MODEL_FACTORY_INJECTIONS = true;

var App = Ember.Application.extend({
  modulePrefix: config.modulePrefix,
  podModulePrefix: config.podModulePrefix,
  Resolver: Resolver,
});

loadInitializers(App, config.modulePrefix);

export default App;
