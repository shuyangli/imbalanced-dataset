import DS from 'ember-data';
import Ember from 'ember';
var inflector = Ember.Inflector.inflector;
inflector.irregular('analysis', 'analyses');

export default DS.Model.extend({
  dataset: DS.belongsTo('dataset', {async: true}),
  classifiers: DS.hasMany('classifier', {async: true}),
  title: DS.attr('string'),
  description: DS.attr('string'),
  classifier_ids: DS.attr(),
  hasHeader: DS.attr('boolean'),
  posLabel: DS.attr('number', {default: 1}),
  completed: DS.attr('boolean'),
  ignoreFirst: DS.attr('boolean'),
  created: DS.attr('date')
});
