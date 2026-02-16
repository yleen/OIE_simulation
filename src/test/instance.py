from simulation.base.structure import TwoTupleTS, TwoTupleS
from simulation.oie.event import Event
from simulation.oie.event_star import EventStar, set_bijection, EventStarS
from simulation.oie.optional_intervals_event import VoidOIE, OIE

oie_void = VoidOIE()


atomEvent_a: Event = Event("atomEvent_DrA")
atomEventStar_a: EventStar = EventStar("atomEvent*_DrA")
set_bijection(atomEvent_a, atomEventStar_a)

atomEvent_b: Event = Event("atomEvent_DrB")
atomEventStar_b: EventStar = EventStar("atomEvent*_DrB")
set_bijection(atomEvent_b, atomEventStar_b)

atomEvent_c: Event = Event("atomEvent_DrC")
atomEventStar_c: EventStar = EventStar("atomEvent*_DrC")
set_bijection(atomEvent_c, atomEventStar_c)

atomEvent_1: Event = Event("atomEvent_1")
atomEventStar_1: EventStar = EventStar("atomEvent*_1")
set_bijection(atomEvent_1, atomEventStar_1)

atomEvent_2: Event = Event("atomEvent_2")
atomEventStar_2: EventStar = EventStar("atomEvent*_2")
set_bijection(atomEvent_2, atomEventStar_2)


atomOie_1 = OIE(p_expr="atomOie_1",
                p_C=(),
                p_F=TwoTupleTS(((1, 2),), ((3, 4),), ((4, 5),)),
                p_I=TwoTupleS((1, 2), (3, 4), (4, 5)),
                p_A=EventStarS(atomEventStar_1))

atomOie_2 = OIE(p_expr="atomOie_2",
                p_C=(),
                p_F=TwoTupleTS(((1, 3),), ((2, 4),), ((3, 5),)),
                p_I=TwoTupleS((1, 3), (2, 4), (4, 5)),
                p_A=EventStarS(atomEventStar_2))

print(atomOie_1)
print(atomOie_2)
