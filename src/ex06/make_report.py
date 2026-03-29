from analytics import Research, Analytics
import config

def make_report():
    research = Research('data.csv')
    data = research.file_reader()

    analytics = Analytics(data)

    heads, tails = analytics.counts()
    total = heads + tails
    head_frac, tail_frac = analytics.fractions(heads, tails)

    predections = analytics.predict_random(config.num_of_steps)
    pred_heads = sum(p[0] for p in predections)
    pred_tails = sum(p[1] for p in predections)

    report = config.report_template.format(
        total=total,
        heads=heads,
        tails=tails,
        head_prob=round(head_frac * 100, 2),
        tail_prob=round(tail_frac * 100, 2),
        steps=config.num_of_steps,
        pred_heads=pred_heads,
        pred_tails=pred_tails
    )

    print(report)
    analytics.save_file(report, 'report', 'txt')

    research.send_telegram("The report has been succesfully created")

if __name__ == '__main__':
    try:
        make_report()
    except Exception as e:
        print(f"Xato: {e}")
        research = Research('data.csv')
        research.send_telegram("The report hasn't been created due to an error")