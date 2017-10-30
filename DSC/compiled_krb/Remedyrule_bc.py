# Remedyrule_bc.py

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
        with engine.prove(rule.rule_base.root_name, 'ar', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.get: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'VM', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "Remedyrule.get: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'PM', context,
                                  (rule.pattern(3),
                                   rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "Remedyrule.get: got unexpected plan from when clause 3"
                    mark4 = context.mark(True)
                    if rule.pattern(4).match_data(context, context,
                           (context.lookup_data('responsefault'),context.lookup_data('VMfault'),context.lookup_data('PMfault'))):
                      context.end_save_all_undo()
                      with engine.prove('Remedy', 'remedy_of', context,
                                        (rule.pattern(4),
                                         rule.pattern(5),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "Remedyrule.get: got unexpected plan from when clause 5"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark4)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def arr(rule, arg_patterns, arg_context):
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
        ft=tuple(context.lookup_data('fault'))
        mark2 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               ft[0]):
          context.end_save_all_undo()
          with engine.prove('Remedy', 'responsekind', context,
                            (rule.pattern(0),
                             rule.pattern(1),)) \
            as gen_3:
            for x_3 in gen_3:
              assert x_3 is None, \
                "Remedyrule.arr: got unexpected plan from when clause 3"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def VM(rule, arg_patterns, arg_context):
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
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               tuple(context.lookup_data('fault'))[1]):
          context.end_save_all_undo()
          with engine.prove('Remedy', 'VMfault', context,
                            (rule.pattern(0),
                             rule.pattern(1),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "Remedyrule.VM: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def PM(rule, arg_patterns, arg_context):
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
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               tuple(context.lookup_data('fault'))[2]):
          context.end_save_all_undo()
          with engine.prove('Remedy', 'PMfault', context,
                            (rule.pattern(0),
                             rule.pattern(1),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "Remedyrule.PM: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('Remedyrule')
  
  bc_rule.bc_rule('get', This_rule_base, 'get',
                  get, None,
                  (contexts.variable('fault'),
                   contexts.variable('remedy'),),
                  (),
                  (contexts.variable('responsefault'),
                   contexts.variable('fault'),
                   contexts.variable('VMfault'),
                   contexts.variable('PMfault'),
                   contexts.variable('finalfault'),
                   contexts.variable('remedy'),))
  
  bc_rule.bc_rule('arr', This_rule_base, 'ar',
                  arr, None,
                  (contexts.variable('responsefault'),
                   contexts.variable('fault'),),
                  (),
                  (contexts.variable('resp'),
                   contexts.variable('responsefault'),))
  
  bc_rule.bc_rule('VM', This_rule_base, 'VM',
                  VM, None,
                  (contexts.variable('VMfault'),
                   contexts.variable('fault'),),
                  (),
                  (contexts.variable('ft'),
                   contexts.variable('VMfault'),))
  
  bc_rule.bc_rule('PM', This_rule_base, 'PM',
                  PM, None,
                  (contexts.variable('PMfault'),
                   contexts.variable('fault'),),
                  (),
                  (contexts.variable('pt'),
                   contexts.variable('PMfault'),))


Krb_filename = '..\\Remedyrule.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 26), (4, 4)),
    ((27, 33), (5, 5)),
    ((34, 40), (6, 6)),
    ((43, 43), (7, 7)),
    ((45, 51), (9, 9)),
    ((66, 70), (13, 13)),
    ((72, 72), (15, 15)),
    ((75, 75), (16, 16)),
    ((77, 83), (18, 18)),
    ((98, 102), (21, 21)),
    ((106, 106), (23, 23)),
    ((108, 114), (25, 25)),
    ((129, 133), (28, 28)),
    ((137, 137), (30, 30)),
    ((139, 145), (32, 32)),
)
