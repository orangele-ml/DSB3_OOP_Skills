num_of_steps = 3

report_template = (
    "We made {total} observations by tossing a coin:\n"
    "{heads} were heads and {tails} were tails.\n"
    "The probabilities are {head_prob}% and {tail_prob}%, respectively.\n"
    "Our forecast is that the next {steps} observations will be: \n"
    "{pred_heads} head and {pred_tails} tails.\n"
)