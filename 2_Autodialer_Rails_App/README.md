# Autodialer App (Ruby on Rails)
## Overview
This app allows automated calling using the Twilio API and AI prompt interface.

### Features
- Upload 100+ numbers
- Auto-call using Twilio
- AI prompt for voice/text commands ("Call 9876543210")
- Call logs

### Setup
```bash
rails new autodialer_app
cd autodialer_app
bundle add twilio-ruby
rails generate scaffold CallLog phone_number:string status:string
rails db:migrate
```

Then in your controller:
```ruby
require 'twilio-ruby'
def make_call
  account_sid = ENV['TWILIO_SID']
  auth_token = ENV['TWILIO_AUTH']
  client = Twilio::REST::Client.new(account_sid, auth_token)
  call = client.calls.create(
    url: 'http://demo.twilio.com/docs/voice.xml',
    to: params[:phone_number],
    from: ENV['TWILIO_NUMBER']
  )
  render json: call
end
```

To integrate AI prompt, use OpenAI API with `ruby-openai` gem.
