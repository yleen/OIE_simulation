# Simulation code for ''Optional intervals event''

**The paper in Arxiv has now been updated to v4, where OIE is defined as a 4-tuple structure. We are currently updating the implementation of this code and will submit it as soon as possible.**

The "Optional Intervals Event" is a newly introduced concept in theoretical research (as seen in arXiv:2504.09471 [math.GM]).
It involves defining events within specific,
customizable time intervals and establishing formal logical operations (like "complete sequential addition/multiplication")
to structure these intervals.

[//]: # (The framework aims to model event ordering abstractly)

# The paper

## Arxiv
<https://arxiv.org/abs/2504.09471>

## Alphaxiv
<https://www.alphaxiv.org/abs/2504.09471>

# Code link
[**(Property 3)** Ordering of starting timestamp and ending timestamp](src/simulation/optional_intervals_event/event.py#44)

[**(Definition 4)** Event with undetermined interval](src/simulation/optional_intervals_event/event_star.py#14)

[**(Definition 6)** Optional Intervals Event](src/simulation/optional_intervals_event/optional_intervals_event.py#17)

[**(Definition 7)** Get the bound 2-tuple of a non-empty finite 2TupleT instance](src/simulation/base/helper.py#33)

[**(Property 5)** Get the bound 2-tuple set from a 2TupleTS instance](src/simulation/base/helper.py#12)

[**(Definition 8)** Equality of OIE instances](src/simulation/optional_intervals_event/optional_intervals_event.py#42)

[**(Definition 11)** Get the set composed of the I(3rd elements) of all OIE instances](src/simulation/optional_intervals_event/optional_intervals_event_set.py#59)

[**(Definition 12)** Void OIE](src/simulation/optional_intervals_event/optional_intervals_event.py#102)

[**(Definition 14)** Get the natural isomorphism to Cartesian product of each element of a 2TupleSS instance according to a certain index order](src/simulation/optional_intervals_event/naturally_isomorphic_to_cartesian_product.py#13)

[**(Definition 15)** Set of tuples of infeasible interval 2-tuples of all members of a finite OIES instance under an index order](src/simulation/optional_intervals_event/optional_intervals_event_set.py#112)

[**(Definition 18/function 1)** Get the minimum 1st item of a 2TupleT instance](src/simulation/base/helper.py#72)

[**(Definition 18/function 2)** Get the maximum 2nd item of a 2TupleT instance](src/simulation/base/helper.py#89)

[**(Definition 19)** Get the domain filtered subset of a 2TupleTS instance in a domain](src/simulation/sequential_operation/addition/domain_filtered_2tupleTS.py#34)

[**(Definition 20)** Complete Sequential Addition](src/simulation/sequential_operation/addition/complete_sequential_addition.py#26)

[**(Definition 21)** Get the ascending order filtered subset of a 2TupleTS instance](src/simulation/sequential_operation/multiplication/complete_asc_order_filtered_2tupleTS.py#11)

[**(Definition 22)** Complete Sequential Multiplication](src/simulation/sequential_operation/multiplication/complete_sequential_multiplication.py#25)

[**(Property 11)** Sequential operations involving identical OIE instances result in a void OIE instance](src/simulation/sequential_operation/helper.py#82)

[**(Property 12)** The sequential operations involving void OIE instances result oie_void](src/simulation/sequential_operation/helper.py#89)

[**(Definition 24)** Natural Complete Sequential Addition](src/simulation/sequential_operation/addition/complete_sequential_addition.py#79)

[**(Definition 27)** The 1st type of implementation of an OIE instance](src/simulation/implement/first_type.py#13)

[**(Definition 28)** The 2nd type of implementation of an OIE instance](src/simulation/implement/second_type.py#14)

[//]: # ([**&#40;Definition 14&#41;** Function to get the set that is naturally isomorphic to the Cartesian)
[//]: # (product of all members of a finite 2TupleSS instance in an index order]&#40;src/simulation/optional_intervals_event/naturally_isomorphic_to_cartesian_product.py#13&#41;)
