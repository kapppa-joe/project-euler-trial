from typing import TypeAlias
from util import all_primes_below, prime_generator, is_prime, join_nums
from itertools import chain

# memo the primes in first 1m for effectively checking larger primes.
memo_size = 1_000_000
prime_ordered_memo = list(all_primes_below(memo_size))
prime_set_memo = set(prime_ordered_memo)

Graph: TypeAlias = dict[int, set[int]]


def p060(set_size: int = 5) -> int:
    prime_gen = chain(prime_ordered_memo, prime_generator(
        start=memo_size, prime_checker=prime_checker))  # a generator for prime numbers

    graph = {}

    for new_prime in prime_gen:
        graph = update_graph(new_prime, graph)
        pair_sets = search_graph_for_pairs_set(
            graph, wanted_size=set_size, curr_node=new_prime)
        if pair_sets != None:
            print(
                f"found a set of size {set_size}: {pair_sets}. The sum is {sum(pair_sets)}")
            return sum(pair_sets)


def prime_checker(num: int) -> bool:
    if num < memo_size:
        return num in prime_set_memo
    else:
        return is_prime(num, known_prime=prime_ordered_memo)


def check_prime_pair(a: int, b: int) -> bool:
    # note: does not test whether a, b, are prime, as I intended to pull those num from a prime generator
    if a == b:
        return False
    ab, ba = join_nums(a, b), join_nums(b, a)
    return is_prime(ab) and is_prime(ba)


def update_graph(new_prime: int, graph: Graph) -> Graph:
    graph[new_prime] = set()

    for prime in graph.keys():
        if check_prime_pair(prime, new_prime):
            graph[prime].add(new_prime)
            graph[new_prime].add(prime)

    return graph


def search_graph_for_pairs_set(graph: Graph, wanted_size: int, curr_node: int, curr_set: set[int] | None = None, seen: set[int] | None = None) -> set[int] | None:
    if curr_set == None:
        curr_set = set()
    if seen == None:
        seen = set()

    curr_set.add(curr_node)
    if len(curr_set) == wanted_size:  # end condiition
        return curr_set

    # find the next node which can pair with any member in current set.
    next_nodes = (node for node in graph[curr_node]
                  if not node in seen
                  and not node in curr_set
                  and curr_set.issubset(graph[node]))

    # traverse the graph recursively. return if a solution was found
    for node in next_nodes:
        solution_found = search_graph_for_pairs_set(
            graph, wanted_size, curr_node=node, curr_set=curr_set, seen=seen)
        if solution_found:
            return solution_found

    # if no solution was found, mark this route as seen
    curr_set.remove(curr_node)
    seen.add(curr_node)
    return None
