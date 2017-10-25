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
        print(context.lookup_data('fault'))
        with engine.prove(rule.rule_base.root_name, 'ar', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_2:
          for x_2 in gen_2:
            assert x_2 is None, \
              "Remedyrule.get: got unexpected plan from when clause 2"
            with engine.prove(rule.rule_base.root_name, 'VM', context,
                              (rule.pattern(2),
                               rule.pattern(1),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "Remedyrule.get: got unexpected plan from when clause 3"
                with engine.prove(rule.rule_base.root_name, 'PM', context,
                                  (rule.pattern(3),
                                   rule.pattern(1),)) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "Remedyrule.get: got unexpected plan from when clause 4"
                    mark5 = context.mark(True)
                    if rule.pattern(4).match_data(context, context,
                           (context.lookup_data('responsefault'),context.lookup_data('VMfault'),context.lookup_data('PMfault'))  ):
                      context.end_save_all_undo()
                      with engine.prove('Remedy', 'remedy_of', context,
                                        (rule.pattern(4),
                                         rule.pattern(5),)) \
                        as gen_6:
                        for x_6 in gen_6:
                          assert x_6 is None, \
                            "Remedyrule.get: got unexpected plan from when clause 6"
                          rule.rule_base.num_bc_rule_successes += 1
                          yield
                    else: context.end_save_all_undo()
                    context.undo_to_mark(mark5)
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
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 ft[0]):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   ft[1]):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     ft[2]):
                context.end_save_all_undo()
                mark5 = context.mark(True)
                if rule.pattern(4).match_data(context, context,
                       ft[3]):
                  context.end_save_all_undo()
                  with engine.prove(rule.rule_base.root_name, 'VMstorage', context,
                                    (rule.pattern(1),
                                     rule.pattern(5),)) \
                    as gen_6:
                    for x_6 in gen_6:
                      assert x_6 is None, \
                        "Remedyrule.VM: got unexpected plan from when clause 6"
                      with engine.prove(rule.rule_base.root_name, 'VMmemory', context,
                                        (rule.pattern(2),
                                         rule.pattern(6),)) \
                        as gen_7:
                        for x_7 in gen_7:
                          assert x_7 is None, \
                            "Remedyrule.VM: got unexpected plan from when clause 7"
                          with engine.prove(rule.rule_base.root_name, 'VMnetwork', context,
                                            (rule.pattern(3),
                                             rule.pattern(7),)) \
                            as gen_8:
                            for x_8 in gen_8:
                              assert x_8 is None, \
                                "Remedyrule.VM: got unexpected plan from when clause 8"
                              with engine.prove(rule.rule_base.root_name, 'VMcpu', context,
                                                (rule.pattern(4),
                                                 rule.pattern(8),)) \
                                as gen_9:
                                for x_9 in gen_9:
                                  assert x_9 is None, \
                                    "Remedyrule.VM: got unexpected plan from when clause 9"
                                  mark10 = context.mark(True)
                                  if rule.pattern(9).match_data(context, context,
                                         (context.lookup_data('f1'),context.lookup_data('f2'),context.lookup_data('f3'),context.lookup_data('f4'))):
                                    context.end_save_all_undo()
                                    with engine.prove('Remedy', 'VMfault', context,
                                                      (rule.pattern(9),
                                                       rule.pattern(10),)) \
                                      as gen_11:
                                      for x_11 in gen_11:
                                        assert x_11 is None, \
                                          "Remedyrule.VM: got unexpected plan from when clause 11"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark10)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark5)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
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
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 ft[0]):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   ft[1]):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     ft[2]):
                context.end_save_all_undo()
                mark5 = context.mark(True)
                if rule.pattern(4).match_data(context, context,
                       ft[3]):
                  context.end_save_all_undo()
                  with engine.prove(rule.rule_base.root_name, 'PMstorage', context,
                                    (rule.pattern(1),
                                     rule.pattern(5),)) \
                    as gen_6:
                    for x_6 in gen_6:
                      assert x_6 is None, \
                        "Remedyrule.PM: got unexpected plan from when clause 6"
                      with engine.prove(rule.rule_base.root_name, 'PMmemory', context,
                                        (rule.pattern(2),
                                         rule.pattern(6),)) \
                        as gen_7:
                        for x_7 in gen_7:
                          assert x_7 is None, \
                            "Remedyrule.PM: got unexpected plan from when clause 7"
                          with engine.prove(rule.rule_base.root_name, 'PMnetwork', context,
                                            (rule.pattern(3),
                                             rule.pattern(7),)) \
                            as gen_8:
                            for x_8 in gen_8:
                              assert x_8 is None, \
                                "Remedyrule.PM: got unexpected plan from when clause 8"
                              with engine.prove(rule.rule_base.root_name, 'PMcpu', context,
                                                (rule.pattern(4),
                                                 rule.pattern(8),)) \
                                as gen_9:
                                for x_9 in gen_9:
                                  assert x_9 is None, \
                                    "Remedyrule.PM: got unexpected plan from when clause 9"
                                  mark10 = context.mark(True)
                                  if rule.pattern(9).match_data(context, context,
                                         (context.lookup_data('f5'),context.lookup_data('f6'),context.lookup_data('f7'),context.lookup_data('f8'))):
                                    context.end_save_all_undo()
                                    with engine.prove('Remedy', 'PMfault', context,
                                                      (rule.pattern(9),
                                                       rule.pattern(10),)) \
                                      as gen_11:
                                      for x_11 in gen_11:
                                        assert x_11 is None, \
                                          "Remedyrule.PM: got unexpected plan from when clause 11"
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
                                  else: context.end_save_all_undo()
                                  context.undo_to_mark(mark10)
                else: context.end_save_all_undo()
                context.undo_to_mark(mark5)
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def VMstorage(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'VMstorage', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.VMstorage: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def VMmemory(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'VMmemory', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.VMmemory: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def VMnetwork(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'VMnetwork', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.VMnetwork: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def VMcpu(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'VMcpu', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.VMcpu: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def PMstorage(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'PMstorage', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.PMstorage: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def PMmemory(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'PMmemory', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.PMmemory: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def PMnetwork(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'PMnetwork', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.PMnetwork: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def PMcpu(rule, arg_patterns, arg_context):
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
        with engine.prove('Remedy', 'PMcpu', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "Remedyrule.PMcpu: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
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
                  (pattern.pattern_literal('ft'),
                   contexts.variable('s1'),
                   contexts.variable('m1'),
                   contexts.variable('p1'),
                   contexts.variable('c1'),
                   contexts.variable('f1'),
                   contexts.variable('f2'),
                   contexts.variable('f3'),
                   contexts.variable('f4'),
                   contexts.variable('Vf'),
                   contexts.variable('VMfault'),))
  
  bc_rule.bc_rule('PM', This_rule_base, 'PM',
                  PM, None,
                  (contexts.variable('PMfault'),
                   contexts.variable('fault'),),
                  (),
                  (pattern.pattern_literal('ft'),
                   contexts.variable('s2'),
                   contexts.variable('m2'),
                   contexts.variable('p2'),
                   contexts.variable('c2'),
                   contexts.variable('f5'),
                   contexts.variable('f6'),
                   contexts.variable('f7'),
                   contexts.variable('f8'),
                   contexts.variable('Pf'),
                   contexts.variable('PMfault'),))
  
  bc_rule.bc_rule('VMstorage', This_rule_base, 'VMstorage',
                  VMstorage, None,
                  (contexts.variable('s1'),
                   contexts.variable('f1'),),
                  (),
                  (contexts.variable('s1'),
                   contexts.variable('f1'),))
  
  bc_rule.bc_rule('VMmemory', This_rule_base, 'VMmemory',
                  VMmemory, None,
                  (contexts.variable('m1'),
                   contexts.variable('f2'),),
                  (),
                  (contexts.variable('m1'),
                   contexts.variable('f2'),))
  
  bc_rule.bc_rule('VMnetwork', This_rule_base, 'VMnetwork',
                  VMnetwork, None,
                  (contexts.variable('p1'),
                   contexts.variable('f3'),),
                  (),
                  (contexts.variable('p1'),
                   contexts.variable('f3'),))
  
  bc_rule.bc_rule('VMcpu', This_rule_base, 'VMcpu',
                  VMcpu, None,
                  (contexts.variable('c1'),
                   contexts.variable('f4'),),
                  (),
                  (contexts.variable('c1'),
                   contexts.variable('f4'),))
  
  bc_rule.bc_rule('PMstorage', This_rule_base, 'PMstorage',
                  PMstorage, None,
                  (contexts.variable('s2'),
                   contexts.variable('f5'),),
                  (),
                  (contexts.variable('s2'),
                   contexts.variable('f5'),))
  
  bc_rule.bc_rule('PMmemory', This_rule_base, 'PMmemory',
                  PMmemory, None,
                  (contexts.variable('m2'),
                   contexts.variable('f6'),),
                  (),
                  (contexts.variable('m2'),
                   contexts.variable('f6'),))
  
  bc_rule.bc_rule('PMnetwork', This_rule_base, 'PMnetwork',
                  PMnetwork, None,
                  (contexts.variable('p2'),
                   contexts.variable('f7'),),
                  (),
                  (contexts.variable('p2'),
                   contexts.variable('f7'),))
  
  bc_rule.bc_rule('PMcpu', This_rule_base, 'PMcpu',
                  PMcpu, None,
                  (contexts.variable('c2'),
                   contexts.variable('f8'),),
                  (),
                  (contexts.variable('c2'),
                   contexts.variable('f8'),))


Krb_filename = '..\\Remedyrule.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 20), (4, 4)),
    ((21, 27), (5, 5)),
    ((28, 34), (6, 6)),
    ((35, 41), (7, 7)),
    ((44, 44), (8, 8)),
    ((46, 52), (9, 9)),
    ((67, 71), (13, 13)),
    ((73, 73), (15, 15)),
    ((76, 76), (16, 16)),
    ((78, 84), (17, 17)),
    ((99, 103), (20, 20)),
    ((107, 107), (22, 22)),
    ((111, 111), (23, 23)),
    ((115, 115), (24, 24)),
    ((119, 119), (25, 25)),
    ((123, 123), (26, 26)),
    ((125, 131), (27, 27)),
    ((132, 138), (28, 28)),
    ((139, 145), (29, 29)),
    ((146, 152), (30, 30)),
    ((155, 155), (31, 31)),
    ((157, 163), (32, 32)),
    ((188, 192), (35, 35)),
    ((196, 196), (37, 37)),
    ((200, 200), (38, 38)),
    ((204, 204), (39, 39)),
    ((208, 208), (40, 40)),
    ((212, 212), (41, 41)),
    ((214, 220), (42, 42)),
    ((221, 227), (43, 43)),
    ((228, 234), (44, 44)),
    ((235, 241), (45, 45)),
    ((244, 244), (46, 46)),
    ((246, 252), (47, 47)),
    ((277, 281), (50, 50)),
    ((283, 289), (52, 52)),
    ((302, 306), (55, 55)),
    ((308, 314), (57, 57)),
    ((327, 331), (60, 60)),
    ((333, 339), (62, 62)),
    ((352, 356), (65, 65)),
    ((358, 364), (67, 67)),
    ((377, 381), (70, 70)),
    ((383, 389), (72, 72)),
    ((402, 406), (75, 75)),
    ((408, 414), (77, 77)),
    ((427, 431), (80, 80)),
    ((433, 439), (82, 82)),
    ((452, 456), (85, 85)),
    ((458, 464), (87, 87)),
)
