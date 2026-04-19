package data

deny[msg] {
 input.destination_country!= "ZA"
 msg := "BLOCKED"
}
