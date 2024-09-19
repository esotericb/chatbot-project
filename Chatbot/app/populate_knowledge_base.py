from app import create_app, db
from app.models import KnowledgeBase

app = create_app()

# Run the script within the app context
with app.app_context():
    # Sample knowledge base entries
    entries = [
        KnowledgeBase(question="How do I pay for water bills?",
                      answer="You can pay your water bills through M-Pesa PayBill No. 772153, KCB Account No. 1273194454, or Cooperative Bank Account No. 01100632410100. Do not give Cash to anyone."),
        KnowledgeBase(question="How do I lodge a billing complaint?",
                      answer="Visit our offices in your respective Area or Scheme. You can also use our USSD Code *873*048# or call us on 0562030355/0799085696 or email us at kacwasco@gmail.com."),
        KnowledgeBase(question="How can I check my bill?",
                      answer="You can check your bill by logging into your account on our website or contacting customer support."),
        KnowledgeBase(question="When disconnected, how do I get reconnected?",
                      answer="You will be required to pay any outstanding bill together with the reconnection fee, this is after visiting our ofices and reviewing your case."),
        KnowledgeBase(question="What is your meter reading schedule?",
                      answer="Our officers read meters from 1st to 14th of every month."),
        KnowledgeBase(question="How do you calculate the water bills?",
                      answer="After a meter is read and the reading submitted, the units consumed are calculated against the approved tariff by our regulator (WASREB). The tariff can be found on our website kakamegawater.co.ke"),
        KnowledgeBase(question="How am I billed the sewer charges?",
                      answer="As directed by the approved Tariff, the sewer charge is billed at 75% of total water consumed."),
        KnowledgeBase(question="Why am I billed on estimate?",
                      answer="This can occur when no reading is captured for your account due to lack of access to the water meter because of a closed gate or fierce dog, or due to a stuck or faulty meter."),
        KnowledgeBase(question="How can I check my bill?",
                      answer="You can check your bill by using our USSD Code *873*048# or contacting customer support."),
        KnowledgeBase(question="How do I get my meter tested and serviced?",
                      answer="You can visit your respective Area or Scheme office and a meter service or meter testing task will be booked and assigned to artisan to undertake the same. You will be required to pay Kshs. 500 for meter testing. Meter servicing is free."),
        KnowledgeBase(question="How do I report pipe bursts, leakages or water theft?",
                      answer="You can report through the USSD Code *873*048#, Call us on 0562030355 or 0799085696, or email us on kacwasco@gmail.com."),
        KnowledgeBase(question="How can I apply for a part payment plan?",
                      answer="You can visit our offices, and you will be required to sign an agreement form and pay at least 50% of the debt.")
    ]

    # Add entries to the database
    for entry in entries:
        db.session.add(entry)

    db.session.commit()
    print("Knowledge base populated successfully!")
