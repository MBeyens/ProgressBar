import progress_tracker, time

amount_total_variants = 123
variant_number = 0
for variant_number in range(amount_total_variants):
    progress_tracker.update_progress(variant_number, amount_total_variants)
    time.sleep(1)
