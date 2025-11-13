<?php

namespace Symfony\Config\UxIcons;

use Symfony\Component\Config\Loader\ParamConfigurator;
use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class IconifyConfig 
{
    private $enabled;
    private $onDemand;
    private $endpoint;
    private $_usedProperties = [];

    /**
     * @default true
     * @param ParamConfigurator|bool $value
     * @return $this
     */
    public function enabled($value): static
    {
        $this->_usedProperties['enabled'] = true;
        $this->enabled = $value;

        return $this;
    }

    /**
     * Whether to download icons "on demand".
     * @default true
     * @param ParamConfigurator|bool $value
     * @return $this
     */
    public function onDemand($value): static
    {
        $this->_usedProperties['onDemand'] = true;
        $this->onDemand = $value;

        return $this;
    }

    /**
     * The endpoint for the Iconify icons API.
     * @default 'https://api.iconify.design'
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function endpoint($value): static
    {
        $this->_usedProperties['endpoint'] = true;
        $this->endpoint = $value;

        return $this;
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('enabled', $value)) {
            $this->_usedProperties['enabled'] = true;
            $this->enabled = $value['enabled'];
            unset($value['enabled']);
        }

        if (array_key_exists('on_demand', $value)) {
            $this->_usedProperties['onDemand'] = true;
            $this->onDemand = $value['on_demand'];
            unset($value['on_demand']);
        }

        if (array_key_exists('endpoint', $value)) {
            $this->_usedProperties['endpoint'] = true;
            $this->endpoint = $value['endpoint'];
            unset($value['endpoint']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['enabled'])) {
            $output['enabled'] = $this->enabled;
        }
        if (isset($this->_usedProperties['onDemand'])) {
            $output['on_demand'] = $this->onDemand;
        }
        if (isset($this->_usedProperties['endpoint'])) {
            $output['endpoint'] = $this->endpoint;
        }

        return $output;
    }

}
