

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(customer, issue):         #open ticket function allows user to open a ticket
    ticket_id = f"Ticket{len(service_tickets) + 1:03}"
    service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}   
    print(f"New ticket opened: {ticket_id}")

def update_status(ticket_id, new_status):           #update status of a ticket in program
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"The status of {ticket_id} has been updated to {new_status}")
    else:
        print(f"The ticket ID {ticket_id} not found")

def display_ticket(status=None):            #displays all tickets
    if status:
        filtered_tickets = {tid: ticket for tid, ticket in service_tickets.items() if ticket["Status"] == status}
        if filtered_tickets:
            print(f"Tickets with status '{status}':")
            for tid, ticket in filtered_tickets.items():
                print(f"{tid}: Customer {ticket['Customer']} - Issue: {ticket['Issue']}")
        else:
            print(f"No tickets found with status '{status}'")
    else:
        print("All tickets:")
        for tid, ticket in service_tickets.items():
            print(f"{tid}: Customer {ticket['Customer']} - Issue: {ticket['Issue']} - Status: {ticket['Status']}")

def main():
    while True:                                             #interface for easier use
        print("\n<<<<<<Ticket Manager>>>>>>")
        print("1. Open New Ticket")
        print("2. Update Ticket Status")
        print("3. Display all Tickets")
        print("4. Filter Tickets By Status")
        print("5. Close Program")

        choice = input("Enter the number that corresponds with what you want to do. (1-5)")

        if choice == "1":
            customer = input("Enter the customer's name ")
            issue = input("Enter a discription of the issue ")
            open_ticket(customer, issue)

        elif choice == "2":
            ticket_id = input("what is your ticketid?: ")
            new_status = input("what is the updated status of the ticket?: ")
            update_status(ticket_id, new_status)

        elif choice == "3":
            display_ticket()

        elif choice == "4":
            status = input("Enter status to filter (open/closed): ")
            display_ticket(status)

        elif choice == "5":
            print("Thank you come again! ")
            break
        else:
            print("Invalid choice. Please enter a number from 1-5. ")

if __name__ == "__main__":
    main()


