# remedyget_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def get(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('remedies', 'remedy_of', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "remedyget.get: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('remedyget')
  
  bc_rule.bc_rule('get', This_rule_base, 'get',
                  get, None,
                  (contexts.variable('fault'),
                   contexts.variable('remedy'),),
                  (),
                  (contexts.variable('fault'),
                   contexts.variable('remedy'),))


Krb_filename = '..\\remedyget.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 26), (4, 4)),
)
